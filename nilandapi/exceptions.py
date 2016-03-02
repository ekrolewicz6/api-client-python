#!/usr/bin/env python
#-*- coding: utf-8 -*-

class NilandException(Exception):
    pass

class BadRequestException(NilandException):

    def __init__(self, data):
        message = ''
        if len(data) > 0:
            for field, errors in data.iteritems():
                data[field] = '[%s] %s' % (field, ', '.join(errors))
            message = (' '.join([value for key, value in data.iteritems()]))
        NilandException.__init__(self, message)

class AuthenticationFailedException(NilandException):
    pass

class ForbiddenException(NilandException):
    pass

class NotFoundException(NilandException):
    pass
