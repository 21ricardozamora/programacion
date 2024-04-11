# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list) -> list:
    sorted_items = items.copy()
    for _ in range(len(sorted_items) - 1):
        for item in range(len(sorted_items) - 1):
            if sorted_items[item + 1] <= sorted_items[item]:
                sorted_items[item + 1], sorted_items[item] = (
                    sorted_items[item],
                    sorted_items[item + 1],
                )
    return sorted_items
