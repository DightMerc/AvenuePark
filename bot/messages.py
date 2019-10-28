#!/usr/bin/env python
# -*- coding: utf-8 -*-
import client

def Messages(user):

    if client.getUserLanguage(user)=="RU":
    
        MESSAGES = {
            'start': client.getMessage(1),
            'language': client.getMessage(2),
            'menu': client.getMessage(3),
            'aboutComplex': client.getMessage(4),
            'location': client.getMessage(5),
            'contact': client.getMessage(6),
            'question': client.getMessage(7),
            'zoneLocation': client.getMessage(8),
            'aboutUs': client.getMessage(9),
            'addService': client.getMessage(10),
            'roomPicture': client.getMessage(11),
            'priceList': client.getMessage(12),
            'realy': client.getMessage(13),
        }
    else:
        MESSAGES = {
            'start': client.getMessage(1),
            'language': client.getMessage(2),
            'menu': client.getMessage(3),
            'aboutComplex': client.getMessage(4),
            'location': client.getMessage(5),
            'contact': client.getMessage(6),
            'question': client.getMessage(7),
            'zoneLocation': client.getMessage(8),
            'aboutUs': client.getMessage(9),
            'addService': client.getMessage(10),
            'roomPicture': client.getMessage(11),
            'priceList': client.getMessage(12),
            'realy': client.getMessage(13),

        }

    return MESSAGES


