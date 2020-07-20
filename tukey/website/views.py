from django.shortcuts import render
<<<<<<< HEAD
import numpy as np
import pandas as pd
from django.http import request

# Global Variable
k = None
n = None
alfa = None
table = None
average = None
variance = None
mq_in = None

# Primary Function
def hello_world(request):
    alfa_list = ['0.01', '0.05', '0.1']

    data = {
        'alfa_list': alfa_list
    }

    return render(request, 'index.html', data)


def create_table(request):
    global k, n, alfa, table
=======


def hello_world(request):
    return render(request, 'index.html')


def create_table(request):
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e
    k = int(request.GET['k'])
    n = int(request.GET['n'])
    alfa = float(request.GET['alfa'])

<<<<<<< HEAD
    alfa_list = ['0.01', '0.05', '0.1']
    items = [k, k * n - k]

    generate_matrix()
    format_table = table.style.format({cell: format_html(cell) for cell in table.columns}).render()
=======
    items = [k, k * n - k]

    list = generate_matrix(n, k)
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e

    data = {'k': k,
            'n': n,
            'alfa': alfa,
<<<<<<< HEAD
            'alfa_list': alfa_list,
            'items': items,
            'table': format_table} # tentar criar método para adicionar input e adicionar id (https://stackoverflow.com/questions/41470817/edit-pandas-dataframe-in-flask-html-page)
=======
            'items': items,
            'list': list}
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e

    return render(request, 'index.html', data)


<<<<<<< HEAD
def calcule_tukey(request):
    global k, n, alfa, table, average, variance, mq_in 

    get_table_values()
    get_average()
    get_variance()
    get_mq()
    
    data = {'k': k,
            'n': n,
            'alfa': alfa,
            'table': table,
            'average': average,
            'variance': variance,
            'mq_in': mq_in}

    return render(request, 'index.html', data)


# Secondary Function
def generate_matrix():
    global table
    table = pd.DataFrame()

    for i in range(1, max(k, n) + 1):
        if n >= i:
            table['T{}'.format(i)] = 0
        if k >= i:
            table.loc[i] = 0

    return table


def get_table_values(list):
    global table
    print(list)
    #table[table == 0] = float(list)
    #for j in range(n):
    #    for i in range(k):
    #        cell = 'cell_' + str(j) + '_' + str(i)      
    #        table[table.column[i]][j] = float(request.GET[cell])
            # ou table[table.column[j]][i] = float(request.GET[cell])
      
    return table


def get_average():
    global average, table
    average = []

    for i in range(max(k, n)):
        average.append(table[table.columns[i]].mean())
    
    return average


def get_variance():
    global variance, table
    variance = []

    for i in range(max(k, n)):
        variance.append(table[table.columns[i]].var() / table[table.columns[i]].size)
  
    return variance


def get_mq():
    global mq_in, variance
    mq_in = sum(variance) / len(variance)
  
    return mq_in


def format_html(cell):
    return '<input name="{}" value="{{}}" type="number" min="0" step=".25" />'.format(cell)
=======
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
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e
