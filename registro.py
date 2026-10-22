#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def validar_documento(documento):
    return documento.isdigit() and len(documento) >= 6


def validar_correo(correo):
    if "@" not in correo:
        return False
    usuario, dominio = correo.split("@", 1)
    return (
        bool(usuario)
        and "." in dominio
        and not dominio.startswith(".")
        and not dominio.endswith(".")
    )


def registrar_usuario(usuarios, documento, nombre, correo):
    if not validar_documento(documento):
        raise ValueError("El documento debe tener al menos 6 dígitos")
    if not validar_correo(correo):
        raise ValueError("El correo no es válido")
    usuarios[documento] = {"nombre": nombre, "correo": correo}
    return usuarios[documento]
