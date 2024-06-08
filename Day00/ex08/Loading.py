def show(j, count):
    x = int(85 * j / count)
    print(f"{(j/count) * 100:.0f}%|{u'█'*x}{('.'*(85 - x))}| \
    {j}/{count}", end='\r', flush=True)


def ft_tqdm(lst: range):
    """
    It reproduces the comportment of the function tqdm
    It shows pourcent and a loading bar
    """
    count = len(lst)
    show(0.1, count)
    for i, item in enumerate(lst):
        yield item
        show(i + 1, count)
