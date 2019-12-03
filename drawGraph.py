import matplotlib.pyplot as plt

if __name__ == "__main__":
    pdata = [0.239, 0.236, 0.237]
    rdata = [0.20, 0.193, 0.194]
    # ndata = [0.27, ]
    ddata = [0.952, 0.97, 0.953]
    cdata = [0.224, ]
    rtdata = []

    pdatam = [0.365, 0.276, 0.276, 0.0055, 0.35]
    rdatam = [0.24, 0.194, 0.194, 0.072, 0.29]
    ndatam = [0.429, 0.424, 0.424, 0., 0.]
    ddatam = [0.965, 0.896, 0.896, 0.998, 0.955]
    cdatam = [0.0738, 0.039, 0.039, 0.084, 0.026]

    # pdatat = [0.233, 0.165, 0.125, 0.101, 0.084, 0.074]
    # rdatat = [0.191, 0.27, 0.307, 0.33, 0.345, 0.362]
    # ddatat = [0.952, 0.937, 0.926, 0.917, 0.909, 0.903]
    #
    # pdatatm = [0.33, 0.167, 0.122, 0.096, 0.079, 0.068, 0.33]
    # rdatatm = [0.224, 0.45, 0.46, 0.69, 0.71, 0.73, 0.154]
    # ddatatm = [0.95, 0.92, 0.88, 0.848, 0.815, 0.788, 0.989]
    labels = ['NBI-context', "Add Time Context", 'Add Location Context']
    labelsm = ['NBI-context', 'Add Loc Factor', 'RENBI', 'UBCF','CCRL']
    # label_t = range(5, 31, 5)
    # plt.plot(label_t, rdatat, marker='*',label='Douban')
    # plt.plot(label_t, rdatatm, marker='*',label='Meetup')
    # plt.bar(range(len(pdatam)),rdatam,tick_label=labelsm)
    plt.bar(range(len(pdata)), rdata, tick_label=labels)
    # plt.bar(range(len(ddata)), ddata, tick_label=labels, label='Inter Diversity in Douban dataset')

    # plt.title('L-Coverage')
    plt.title('Different Context Performance')
    plt.xlabel('Algorithm Name')
    plt.ylabel('Recall@5')
    plt.legend()
    plt.grid()
    plt.show()