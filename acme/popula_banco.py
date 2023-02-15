from client.models import Client, Branch

def popula():
    client_dict = [
    {
        'cnpj': '01123456000110',
        'name': 'Acme Inc.',
        'active': True
    },
    {
        'cnpj': '01123456000220',
        'name': 'Coca cola Industrias Ltda',
        'active': True
    },
    {
        'cnpj': '01123456000330',
        'name': 'Latam Airlines Brasil',
        'active': False
    }
]
    for c in client_dict:
        c1 = Client.objects.create(**c)
        c1.save()
    return 'Deu bom'

def popula_branch():
    clien_entry = Client.objects.get(pk=1)
    branch_dict = [
        {
            'cnpj': '01123456000113',
            'name': 'São Paulo',
            'active': True,
            'client_id': clien_entry
        },
        {
            'cnpj': '01123456000112',
            'name': 'xpto',
            'active': True,
            'client_id': clien_entry
        },
        {
            'cnpj': '01123456000114',
            'name': 'taubaté',
            'active': True,
            'client_id': clien_entry
        },
    ]

    for b in branch_dict:
        b1 = Branch.objects.create(**b)
        b1.save()
    return 'Deu bom'