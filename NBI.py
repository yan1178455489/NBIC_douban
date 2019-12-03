# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:42:53 2018

@author: icruicks
"""
import sys

import time
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np
import math

class NBI(BaseEstimator, ClassifierMixin):
    
    def __init__(self):
        pass

    def fit(self, A):
        '''
        A is a biaprtite network of two not neccesarily equal dimensions and a numpy 
        array of binary data
        '''
        A = np.asanyarray(A)
        k_x = np.sum(A, axis=0)#项目的参与数 按列加
        k_y = np.sum(A, axis=1)#用户的参与数 按行加
        W = np.zeros((A.shape[1], A.shape[1]))
        for i in range(W.shape[0]):
            for j in range(W.shape[1]):
                if  k_x[j] != 0:
                    W[i,j] = 1/k_x[j] * np.sum(np.divide(np.multiply(A[:,i],A[:,j]), np.where(k_y > 0,k_y,1)))
        self.W_ =W
        return self
    
    def predict(self, a):
        
        a = np.asanyarray(a)
        f_prime = np.zeros(a.shape[0])
        
        for j in range(f_prime.shape[0]):
            f_prime[j] = np.sum(np.multiply(self.W_[j,:], a))
        
        self.y_ = f_prime
        return self.y_

def getTopN(predict_mat, u_cand):
    topn_ratings = []
    for i in u_cand:
        topn_ratings.append([predict_mat[i],i])
    topn_ratings.sort(reverse=True)
    return topn_ratings

def cos(p,q):
    fenzi = np.dot(p, q)
    fenmu1 = np.sqrt(p.dot(p))
    fenmu2 = np.sqrt(q.dot(q))
    if fenmu1 * fenmu2 != 0:
        return fenzi / (fenmu1 * fenmu2)

if __name__ == '__main__':
    ufactor = input('ufactor:')
    ufactor = float(ufactor)
    tagfactor = input('tagfactor:')
    tagfactor = float(tagfactor)
    hfactor = input('hfactor:')
    hfactor = float(hfactor)
    lcfactor = input('lcfactor:')
    lcfactor = float(lcfactor)
    tmfactor = input('tmfactor:')
    tmfactor = float(tmfactor)
    top_n = input('top_n:')
    top_n = int(top_n)

    time_start = time.time()
    file_path = 'douban/u.data'
    all_file = open(file_path, 'r')
    all_data = []
    for line in all_file:
        data = line.split(' ')
        uid = int(data[0])
        mid = int(data[1])
        all_data.append([uid, mid])
    all_file.close()

    file_path = 'douban/u1.base'
    train_file = open(file_path, 'r')
    train_data = []
    for line in train_file:
        data = line.split(' ')
        uid = int(data[0])
        mid = int(data[1])
        train_data.append([uid, mid])
    train_file.close()

    file_path = 'douban/u1.test'
    test_file = open(file_path, 'r')
    test_data = []
    for line in test_file:
        data = line.split(' ')
        uid = int(data[0])
        mid = int(data[1])
        test_data.append([uid, mid])
    test_file.close()

    events_map = {}
    user_map = {}
    all_data = np.array(all_data)
    u_num = 1 + max(all_data[:,0])
    i_num = 1 + max(all_data[:,1])
    # print(u_num)
    # print(i_num)
    ue = np.zeros((u_num,i_num))
    for tuple in train_data:
        ue[tuple[0]][tuple[1]] = 1

    ue_all = np.zeros((u_num, i_num))
    for data in all_data:
        ue_all[data[0]][data[1]] = 1

    u_cand = []
    u_train = []
    for u in range(u_num):
        u_cand.append([])
        u_train.append([])
    for u in range(u_num):
        for i in range (i_num):
            if ue[u][i] != 1:
                u_cand[u].append(i)
            else:
                u_train[u].append(i)

    # # 地点活动文件
    # le = []
    # et_file = open('douban/location_event.csv', 'r')
    # for line in et_file:
    #     data = line.split(',')
    #     le.append([int(data[0]), int(data[1])])
    # et_file.close()
    # le = np.array(le)
    # location_num = max(le[:, 0]) + 1
    # loc_event = np.zeros((location_num, i_num))
    # for line in le:
    #     if line[1] >= i_num:
    #         continue
    #     loc_event[line[0]][line[1]] = 1
    # # 时间活动文件
    # time_e = []
    # et_file = open('douban/time_event.csv', 'r')
    # for line in et_file:
    #     data = line.split(',')
    #     time_e.append([int(data[0]), int(data[1])])
    # et_file.close()
    # time_e = np.array(time_e)
    # time_num = max(time_e[:, 0]) + 1
    # time_event = np.zeros((time_num, i_num))
    # for line in time_e:
    #     if line[1] >= i_num:
    #         continue
    #     time_event[line[0]][line[1]] = 1

    nbi = NBI()
    # nbi1 = NBI()
    nbi2 = NBI()
    # nbi3 = NBI()
    # nbi4 = NBI()

    # nbi3.fit(loc_event)
    # nbi4.fit(time_event)
    # np.savetxt("douban_result/locW.txt", nbi3.W_)
    # np.savetxt("douban_result/timeW.txt", nbi4.W_)
    # sys.exit()
    # input("done!")

    participant_list = []
    for i in range(i_num):
        participant_list.append([])
    for ratingtuple in train_data:
        (i, j) = ratingtuple
        participant_list[j].append(i)
    u_testset = []
    for u in range(u_num):
        u_testset.append([])
    for tuple in test_data:
        u_testset[tuple[0]].append(tuple[1])

    nbi.W_ = np.loadtxt("douban_result/W.txt")
    # nbi1.W_ = np.loadtxt("douban_result/typeW.txt")
    nbi2.W_ = np.loadtxt("douban_result/hostW.txt")
    # nbi3.W_ = np.loadtxt("douban_result/locW.txt")
    # nbi4.W_ = np.loadtxt("douban_result/timeW.txt")
    nbi.W_ = nbi.W_ - 0.75 * np.multiply(nbi.W_,nbi.W_)
    # nbi1.W_ = nbi1.W_ - 0.75 * np.multiply(nbi1.W_, nbi1.W_)
    nbi2.W_ = nbi2.W_ - 0.75 * np.multiply(nbi2.W_, nbi2.W_)
    # nbi3.W_ = nbi3.W_ - 0.75 * np.multiply(nbi3.W_, nbi3.W_)
    # nbi4.W_ = nbi4.W_ - 0.75 * np.multiply(nbi4.W_, nbi4.W_)
    predict_ratings = np.zeros((u_num,i_num))
    Precision = 0
    Recall = 0
    Novelty = 0
    hits = 0
    recommend_list = []

    for u in range(u_num):
        predict_ratings[u] = ufactor*nbi.predict(ue[u])+hfactor*nbi2.predict(ue[u])
        #+tmfactor*nbi4.predict(ue[u])+lcfactor*nbi3.predict(ue[u])+tagfactor*nbi1.predict(ue[u])
        tmp = getTopN(predict_ratings[u], u_cand[u])[:top_n]
        sub_list = []
        for j in tmp:
            sub_list.append(j[1])
        recommend_list.append(sub_list)

    inter_div = 0
    for u in range(u_num-1):
        for t in range(u+1,u_num):
            common_list = [i for i in recommend_list[u] if i in recommend_list[t]]
            inter_div += 1 - len(common_list)/top_n
    inter_div /= (u_num*(u_num-1))/2

    intra_div = 0
    result_set = set()
    for i in range(u_num):
        if len(u_testset[i]) > 1:
            for j in range(top_n):
                for k in range(j + 1, top_n):
                    intra_div += cos(ue_all[:, recommend_list[i][j]], ue_all[:, recommend_list[i][k]])
                result_set.add(recommend_list[i][j])
                if recommend_list[i][j] in u_testset[i]:
                    hits += 1
                if len(participant_list[recommend_list[i][j]]) > 0:
                    Novelty += -math.log(len(participant_list[recommend_list[i][j]]) / (u_num - 1), 2)
            Precision += top_n
            Recall += len(u_testset[i])
    print(hits)

    Novelty = Novelty / top_n / u_num
    Precision = hits / Precision
    Recall = hits / Recall
    intra_div /= (u_num * top_n * (top_n - 1) / 2)

    print('runtime=', time.time()-time_start)
    print('precision=', Precision)
    print('recall=', Recall)
    print('novelty=', Novelty)
    print('inter_div=', inter_div)
    print('intra_div=', intra_div)
    print('coverage=', len(result_set)/i_num)
