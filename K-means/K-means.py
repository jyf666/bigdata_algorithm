import math
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
c1 = (200.0, 40.0)  # kordinat cluster1
c2 = (100.0, 30.0)  # kordinat cluster2


def hitung():
    count = 0  # coxunt sebagai temp untuk pengecekan loop pertama
    c1cluster = []  # list buat nampung anggota cluster 1
    c2cluster = []  # list buat nampung anggota cluster 2
    tempc1valueclusterx = []
    tempc1valueclustery = []
    tempc2valueclusterx = []
    tempc2valueclustery = []
    tempc1 = ()
    tempc2 = ()
    global c1
    global c2

    with open('dataset.csv') as f:
        tempc1 = c1
        tempc2 = c2
        for line in f:
            count = count + 1
            if count == 1:  # cek disini, kalo baris pertama maka diskip, karena itu judul
                continue
            else:
                x = line.split(',')
                # x[3]->data jumlah siswa
                # x[4]->data jumlah murid

                valc1 = math.sqrt(((float(x[3]) - c1[0]) ** 2) + ((float(x[4]) - c1[1]) ** 2))
                valc2 = math.sqrt(((float(x[3]) - c2[0]) ** 2) + ((float(x[4]) - c2[1]) ** 2))
                if valc1 < valc2:
                    # c1cluster.append(x[0])
                    tempc1valueclusterx.append(float(x[3]))
                    tempc1valueclustery.append(float(x[4]))
                elif valc2 < valc1:
                    # c2cluster.append(x[0])
                    tempc2valueclusterx.append(float(x[3]))
                    tempc2valueclustery.append(float(x[4]))
                else:
                    # c1cluster.append(x[0])
                    tempc1valueclusterx.append(float(x[3]))
                    tempc1valueclustery.append(float(x[4]))

        if tempc1valueclusterx and tempc1valueclustery and tempc2valueclusterx and tempc2valueclustery:
            c1 = (float(sum(tempc1valueclusterx) / float(len(tempc1valueclusterx))),
                  float(sum(tempc1valueclustery) / float(len(tempc1valueclustery))))
            c2 = (float(sum(tempc2valueclusterx) / len(tempc2valueclusterx)),
                  float(sum(tempc2valueclustery) / len(tempc2valueclustery)))

            if c1 != tempc1 and c2 != tempc2:
                print("Cluster 1: ", c1)
                print("Cluster 2: ", c2)
                print("===========")
                tempc1valueclusterx = []
                tempc1valueclustery = []
                tempc2valueclusterx = []
                tempc2valueclustery = []
                hitung()
            else:

                plt.plot(tempc1valueclusterx, tempc1valueclustery, 'o')
                plt.plot(tempc2valueclusterx, tempc2valueclustery, 'o')
                plt.plot(c1[0], c1[1], 'ro')
                plt.plot(c2[0], c2[1], 'ro')
                print("Cluster 1: ", c1)
                print("Cluster 2: ", c2)
                print("STOP!!")
        else:
            print("Cluster Kurang Tepat")


print(hitung())

ax.set_title('K-Means Clustering')
plt.show()