def ft_tqdm(lst: range) -> None:
    """
    Mimics the behavior of the tqdm progress bar for iterating over a list.

    This function takes a list (or any iterable) and displays a progress bar
    in the terminal as it iterates over the items. It prints the percentage of
    completion, a visual progress bar, and the current iteration number. The
    progress bar is dynamically updated on the same line during iteration.
    """
    total = len(lst)
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        bar_length = 50
        filled_length = int(bar_length * progress)
        bar = '=' * filled_length + '>' + '-' * (bar_length - filled_length)
        print(f'\r{progress * 100:.0f}%|[{bar}]| {i+1}/{total}', end='')
        yield item
    print()
