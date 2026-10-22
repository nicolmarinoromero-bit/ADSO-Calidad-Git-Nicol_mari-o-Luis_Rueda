#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def listar_usuarios(usuarios):
    return sorted(
        (
            {
                "documento": documento,
                "nombre": datos["nombre"],
                "correo": datos["correo"],
            }
            for documento, datos in usuarios.items()
        ),
        key=lambda usuario: usuario["nombre"].lower(),
    )


def contar_por_dominio(usuarios):
    conteo = {}
    for datos in usuarios.values():
        dominio = datos["correo"].split("@")[-1]
        conteo[dominio] = conteo.get(dominio, 0) + 1
    return conteo


def generar_resumen(usuarios):
    total = len(usuarios)
    dominios = contar_por_dominio(usuarios)
    detalle = ", ".join(
        f"{dominio}: {cantidad}"
        for dominio, cantidad in sorted(dominios.items())
    )
    return f"Usuarios registrados: {total}. Por dominio: {detalle or 'sin datos'}"
