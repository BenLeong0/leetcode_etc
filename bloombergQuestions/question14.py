def topologicalSort(emps, reps):
    # find source
    u = 'CEO'

    # sort roles
    people = {}
    tsort = []
    def DFS(v):
        for u in reps:
            if reps[u] == v:
                DFS(u)
        tsort.append(v)
        people[v] = []
    DFS(u)

    for (emp, role) in emps:
        people[role].append((emp,role))

    ranking = []
    for role in tsort:
        ranking += people[role]

    return ranking


emps = [('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')]
reps = {'CTO': 'CEO', 'Manager': 'CTO', 'Engineer': 'Manager', 'CFO': 'CEO'}

print(topologicalSort(emps, reps))
