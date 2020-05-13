from django.shortcuts import render


def hello_world(request):
    return render(request, 'index.html')


def create_table(request):
    k = int(request.GET['k'])
    n = int(request.GET['n'])
    alfa = float(request.GET['alfa'])

    items = [k, k * n - k]

    list = generate_matrix(n, k)

    data = {'k': k,
            'n': n,
            'alfa': alfa,
            'items': items,
            'list': list}

    return render(request, 'index.html', data)


def generate_matrix(n, k):
    row = []
    list = []
    first = True

    for j in range(n + 1):
        if first:
            row.append('Repetições')
        else:
            row.append('{}'.format(j))

        for i in range(k):
            if first:
                row.append('T{}'.format(i + 1))
            else:
                row.append('')

        list.append(row)
        row = []
        first = False
    return list

def average(request):

    #

    return render(request, 'index.html')
