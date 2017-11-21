# -*- coding: utf-8 -*-
from .util import get_info
from .models import (Telefono, Email, Direccion)


def processors(request):
    info = get_info()
    telefonos = Telefono.objects.order_by('position')
    correos = Email.objects.order_by('position')
    direcciones = Direccion.objects.order_by('position')

    return {
        'info': info,
        'telefonos': telefonos,
        'correos': correos,
        'direcciones': direcciones,
    }
