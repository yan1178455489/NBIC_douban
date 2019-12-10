import matplotlib.pyplot as plt

if __name__ == "__main__":
    # pdata = [0.24, 0.106, 0.107, 0.22, 0.23]
    # rdata = [0.20, 0.087, 0.088, 0.18, 0.19]
    # ndata = [0.29, 0.286, 0.28, 0.27, 0.27]
    # ddata = [0.952, 0.96, 0.95, 0.85, 0.86]
    # cdata = [0.084, 0.097, 0.092, 0.10, 0.11]
    # rtdata = [747, 607, 599, 845, 764]
    #
    # pdatam = [0.365, 0.276, 0.276, 0.0055, 0.35]
    # rdatam = [0.24, 0.194, 0.194, 0.072, 0.29]
    # ndatam = [0.429, 0.424, 0.424, 0., 0.]
    # ddatam = [0.965, 0.896, 0.896, 0.998, 0.955]
    # cdatam = [0.0738, 0.039, 0.039, 0.084, 0.026]

    pdata = [0.24, 0.106, 0.22]
    rdata = [0.20, 0.087, 0.18]
    ddata = [0.952, 0.96, 0.85]
    rtdata = [747, 798, 760]
    # ddatatm = [0.95, 0.92, 0.88, 0.848, 0.815, 0.788, 0.989]
    # labels = ['NBI', "Add Time Context", 'Add Topic Context', 'Add Location Context', 'Add Host Context']
    labels = ['NBI', "Add Time Context", 'Add Location Context']
    labelsm = ['NBI-context', 'NBI', 'RENBI', 'UBCF','CCRL']
    # label_t = range(5, 31, 5)
    # plt.plot(label_t, rdatat, marker='*',label='Douban')
    # plt.plot(label_t, rdatatm, marker='*',label='Meetup')
    # plt.bar(range(len(pdatam)),rdatam,tick_label=labelsm)
    plt.bar(range(len(pdata)), rtdata, tick_label=labels)
    # plt.bar(range(len(ddata)), ddata, tick_label=labels, label='Inter Diversity in Douban dataset')

    # plt.title('L-Coverage')
    plt.title('Different Context Performance')
    plt.xlabel('Algorithm Name')
    plt.ylabel('Run Time@5')
    plt.legend()
    plt.grid()
    plt.show()