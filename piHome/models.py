#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-12 01:49:03
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-16 22:51:38

from passlib.apps import custom_app_context as pwd_context

from piHome import db
from piHome.config import APP_STATIC
from sqlalchemy_utils import JSONType, PhoneNumberType, ChoiceType
from datetime import datetime

pi_roles = db.Table('pi_roles',
                db.Column('pi_id', db.Integer(),
                    db.ForeignKey('pi.id')),
                db.Column('rolepi_id', db.Integer(),
                    db.ForeignKey('role_pi.id')))

user_notifications = db.Table('user_notifactions',
                         db.Column('user_id', db.Integer(),
                            db.ForeignKey('user.id')),
                         db.Column('notification_id', db.Integer(),
                            db.ForeignKey('notification.id')))

class Pi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    ip = db.Column(db.String(16), unique=True)
    desc = db.Column(db.String(80))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    roles = db.relationship('RolePi', secondary=pi_roles,
                                    backref=db.backref('roles', lazy='dynamic'))
    location = db.relationship('Room', backref='room')

    def __init__(self, name, ip, desc, room_id):
        self.name = name
        self.ip = ip
        self.desc = desc
        self.room_id = room_id

    def __str__(self):
        return u'Pi: {}, Located: {}'.format(self.name, self.location)
    def __repr__(self):
        return u'<Pi: {}, Located: {}>'.format(self.name, self.location)

class RolePi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(255))
    pin_list = db.Column(db.PickleType)
    pi = db.relationship('Pi', secondary=pi_roles,
                                backref=db.backref('pis', lazy='dynamic'))

    def __repr__(self):
        return u'<Pi Role: {}>'.format(self.name)
    def __init__(self, name, desc, pins=[]):
        self.name = name
        self.desc = desc
        self.pin_list = pins
    def __str__(self):
        return self.name

class Notification(db.Model):
    COLOURS = [
            (1, (u'Red')),
            (2, (u'Green')),
            (3, (u'Blue')),
            (4, (u'Violet')),
            (5, (u'Yellow')),
            (6, (u'Cyan')),
            (7, (u'Rainbow'))
            ]
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))
    email = db.Column(db.Boolean)
    text = db.Column(db.Boolean)
    light = db.Column(db.Boolean)
    colour = db.Column(ChoiceType(COLOURS, impl=db.Integer()))
    user_list = db.relationship('User', secondary=user_notifications,
                                        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, desc=u'A notification'):
        self.desc = desc
        self.email = False
        self.text = False
        self.light = True
        self.colour = 3
    def __repr__(self):
        typeList = []
        if self.email:
           typeList.append("Email")
        elif self.text:
            typeList.append("Text")
        elif self.light:
            typeList.append("Light")
        return '<A {} , {} for {}>'.format(typeList, self.desc, self.user_list)
    def __str__(self):
        return self.desc

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    desired_temp = db.Column(db.Float)

    def __repr__(self):
        return '<Room: {}>'.format(self.name)
    def __str__(self):
        return self.name

class HomeDataType(db.Model):
    '''
    Used to describe a JSON Blob stored in HomeData
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    desc = db.Column(db.String(255))

    def __str__(self):
        return u'DataType: {}, {}'.format(self.name, self.desc)
    def __repr__(self):
        return '<DataType: {}>'.format(self.name)

class HomeData(db.Model):
    '''
    Generic storage table for JSON Blobs - organized by Room, Type, Date
    '''
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    json_data = db.Column(JSONType)
    type_id = db.Column(db.Integer, db.ForeignKey('home_data_type.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    type = db.relationship('HomeDataType', backref=db.backref('home_data'))
    room = db.relationship('Room', backref=db.backref('home_data'))

    def __init__(self, room_id):
        self.date_time = datetime.now()
        self.room_id = room_id
    def __repr__(self):
        date = self.date_time.strftime("%A %d. %B %Y")
        return u'<HomeData from: {} at {}>'.format(self.room, date)
    def __str__(self):
        return u'HomeData: {} from {}'.format(self.type.name, self.date_time)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean)
    phone_num = db.Column(PhoneNumberType(country_code='CA'))
    notification = db.relationship('Notification', secondary=user_notifications,
                            backref=db.backref('notifications', lazy='dynamic'))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, username, passw, admin=False):
        self.username = username
        self.password_hash = pwd_context.encrypt(passw)
        self.admin = admin

    def __repr__(self):
        return u'<User {}>'.format(self.username)
    def __str__(self):
        return self.username
