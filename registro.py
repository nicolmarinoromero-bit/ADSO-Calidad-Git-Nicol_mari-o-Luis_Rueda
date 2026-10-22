#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def validar_documento(documento):
    return documento.isdigit() and len(documento) >= 6


def validar_correo(correo):
    if correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    return (
        bool(usuario)
        and "." in dominio
        and not dominio.startswith(".")
        and not dominio.endswith(".")
    )


def buscar_usuario(usuarios, documento):
    documento = documento.strip()
    if documento not in usuarios:
        raise ValueError("No existe un usuario con ese documento")
    return usuarios[documento]


def registrar_usuario(usuarios, documento, nombre, correo):
    documento = documento.strip()
    nombre = nombre.strip()
    correo = correo.strip().lower()
    if documento in usuarios:
        raise ValueError("Ya existe un usuario con ese documento")
    if not validar_documento(documento):
        raise ValueError("El documento debe tener al menos 6 dígitos")
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    if not validar_correo(correo):
        raise ValueError("El correo no es válido")
    usuarios[documento] = {"nombre": nombre, "correo": correo}
    return usuarios[documento]
