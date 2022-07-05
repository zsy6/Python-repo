'''
get&add&delete webhooks in gitlab projects
'''
import sys
import time
import gitlab
import requests
import xlrd
import numpy as np


GITLAB_URL = 'http://****'
#the domain of gitlab
PRIVATE_TOKEN = '****'
#one's access token

def get_column(col):
    '''
    get data from xls table - column
    '''
    x_data = xlrd.open_workbook("system_project_add_hooks.xls")
    sheet = x_data.sheet_by_index(0)
    col_data = sheet.col_values(col)
    #剔除表头元素
    col_data.pop(0)
    #转为整数-project id
    col_data_int = np.asarray(col_data,dtype = int)
    #for i in col_data_int:
        #print(i)
    #print(col_data_int)
    #返回一个Numpy数组
    return col_data_int

def get_hooks(token,project_id,url):
    '''
    获取一个项目的hooks,返回已存在的webhooks集合
    '''
    res = requests.get(url +'/api/v4/projects/{}/hooks?per_page=100'.format(project_id),headers={"PRIVATE-TOKEN":token}).json()
    #webhooks信息的数组  per_page默认值是20
    #返回的可能是找不到project or 空数组
    # {'message': '404 Project Not Found'}
    #if(res.get('message') == '404 Project Not Found'):
        #print("project not exist")
    #{'message': '401 Unauthorized'} 还遇到这个
    if isinstance(res,dict):
        print(res)
    elif not res:
        print("project has no webhook")
    else:
        # for hook in res:
        #     print(hook)
        return res
        #返回已存在的webhooks集合


def add_hooks(token,list_to_add,hook_url):
    '''
    向project_list里的项目添加web_hooks
    需要校验是否已经添加过
    '''
    print("需要添加的项目：--------")
    print(list_to_add)
    for project_id in list_to_add[:]:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(project_id)
        hooks = get_hooks(token,project_id,GITLAB_URL)
        if not hooks:
            continue
        #返回为空就继续查下一个project
        for hook in hooks:
            hook_url_existed = hook.get('url')
            #已经存在的webhooks的url与需要添加的相同(只需要有一条)
            if hook_url_existed == hook_url:
                print(hook_url_existed)
                print(project_id)
                list_to_add.remove(project_id)
                print(list_to_add)
                break
    #最后需要添加webhooks的项目
    print("----------------finally-list-to-add-------------------")
    print(list_to_add)

    data = {"url":hook_url,"push_events":"true","tag_push_events":'True'}# 参数（包括url，事件）
    for project_id in list_to_add:
        res = requests.post(GITLAB_URL +'/api/v4/projects/{}/hooks'.format(project_id),headers={"PRIVATE-TOKEN":token},data=data).json()
        #打印添加webhooks的时间与返回
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("add a webhook")
        print(res)


def delete_hooks(token,list_to_delete,hook_url,remian_hooks):
    '''
    传入需要删除的hook_url 以及项目列表
    如果这个url对应多个webhooks 则需要删除多个webhooks
    remian_hooks代表同一个url需要保留的数量 传入大于等于0的整数
    '''
    for project_id in list_to_delete:
        count = 0
        print("Now in project "+str(project_id))
        hooks = get_hooks(token,project_id,GITLAB_URL)
        #get_hooks的接口默认只能返回20个 因此调整了gethooks的per_page数量
        print("hooks")
        print(hooks)
        if not hooks:
            continue
        for hook in hooks:
            if hook.get('url') == hook_url:
                count += 1
                if count > remian_hooks:
                    hook_id_to_delete = hook.get('id')
                    res = requests.delete(GITLAB_URL+'/api/v4/projects/{}/hooks/{}'.format(project_id,hook_id_to_delete),headers={"PRIVATE-TOKEN":token})
                    #打印删除webhooks的时间以及响应
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    print("删除webhooks")
                    print(count)
                    print(res)
    

if __name__ == "__main__":
    #输出重定向到目录下文件
    # f = open('delete-webhooks.log','a',encoding='utf-8')
    # sys.stdout = f
    # sys.stderr = f

    project_list = get_column(1)

    #print(type(project_list))
    #numpy->list
    project_list_to_operate = list(project_list)
    #print(type(project_list_to_operate))

    #print(project_list_to_operate)
    delete_hooks(PRIVATE_TOKEN,project_list_to_operate,'hook_url_need_to_delete',1)
    
