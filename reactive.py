from rx import of, operators as op

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

source.pipe(
    op.map(lambda s: len(s)),
    op.filter(lambda i: i >= 5)
).subscribe(lambda k: print(f"Received {k}"))



source.pipe(
    op.map(lambda s: (s, list(reversed(s)))),
).subscribe(
    on_next=lambda value: print(f"Original: {value[0]}, Reversed: {''.join(value[1])}"),
    on_completed=lambda: print("Completed")
)


original_list = ["asd", "fgh", "jkl", "qwert", "zxc"]

reversed_list = list(map(lambda x: x, reversed(original_list)))

print(reversed_list)
