from matplotlib import pyplot as plt


def parret_set(k1: dict, direction_k1: bool, name_k1: str, k2: dict, direction_k2: bool, name_k2: str) -> set:
    items = set(k1.keys())
    removed_items = set()

    in_graph_k1 = [k1[c] for c in items]
    in_graph_k2 = [k2[c] for c in items]

    for item in k1.keys():
        for other_item in k1.keys():
            if item == other_item: continue
            cond1 = k1[item] > k1[other_item] if direction_k1 else k1[item] < k1[other_item]
            cond2 = k2[item] > k2[other_item] if direction_k2 else k2[item] < k2[other_item]
            if cond1 and cond2 and other_item in items:
                print(f"{item} доминирует {other_item} по обоим критериям")
                items.remove(other_item)
                removed_items.add(other_item)

    graph_k1 = [k1[c] for c in items]
    graph_k2 = [k2[c] for c in items]

    plt.plot(in_graph_k1, in_graph_k2, ".", color="red")
    #for item in removed_items:
        #plt.annotate(f"Отброшено по Паррету\n{item}", xy=(k1[item], k2[item]))

    plt.plot(graph_k1, graph_k2, ".", color="black")

    plt.xlabel(name_k1)
    plt.ylabel(name_k2)
    for item in items:
        plt.annotate(f"{item}", xy=(k1[item], k2[item]))
    plt.show()
    return items
