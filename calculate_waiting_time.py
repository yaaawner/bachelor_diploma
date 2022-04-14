from flow_model import Flow
from flow_model import StatsInfo
import scipy.stats as sps

def priority_waiting_time(flow_list, pr):
    # priority sort
    flow_list.sort(key=lambda flow: flow.priority)
    sigma = 0
    sigma_prev = 0
    alpha_sum = 0
    beta = 0
    for i in range(pr):
        sigma_prev = sigma
        sigma += flow_list[i].ro
        print(i, sigma)
        if (i != pr - 1):
            alpha_sum += (flow_list[i].ro ** 2) * flow_list[pr - 1].lambda_a * \
                         (flow_list[i].arrival.scv + flow_list[i].service.scv) / flow_list[i].lambda_a
        if (i != 0):
            beta += (flow_list[i].ro ** 2) * flow_list[pr - 1].lambda_a * \
                        (flow_list[i].service.scv + 1) / flow_list[i].lambda_a

    alpha = flow_list[pr - 1].ro * (flow_list[pr - 1].service.scv + 1)
    length = flow_list[pr - 1].ro + flow_list[pr - 1].ro * (flow_list[pr - 1].arrival.scv - 1) / (2 * (1 - sigma)) + \
             (alpha + beta) / ((1 - sigma) * (1 - sigma_prev))
    return length / flow_list[pr - 1].lambda_a


flow_list = []
for i in range(3):
    flow_list.append(Flow(StatsInfo(sps.pareto(b=3)), StatsInfo(sps.pareto(b=3)), 3-i, 1.0))

print(priority_waiting_time(flow_list, 3))