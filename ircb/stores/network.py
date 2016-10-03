# -*- coding: utf-8 -*-
from ircb.lib.constants.signals import (STORE_NETWORK_CREATE,
                                        STORE_NETWORK_CREATED,
                                        STORE_NETWORK_UPDATE,
                                        STORE_NETWORK_UPDATED,
                                        STORE_NETWORK_GET,
                                        STORE_NETWORK_GOT)
from ircb.models import get_session, User, Network
from ircb.stores.base import BaseStore

session = get_session()


class NetworkStore(BaseStore):
    CREATE_SIGNAL = STORE_NETWORK_CREATE
    CREATED_SIGNAL = STORE_NETWORK_CREATED
    GET_SIGNAL = STORE_NETWORK_GET
    GOT_SIGNAL = STORE_NETWORK_GOT
    UPDATE_SIGNAL = STORE_NETWORK_UPDATE
    UPDATED_SIGNAL = STORE_NETWORK_UPDATED

    @classmethod
    def get(cls, query):
        if isinstance(query, dict):
            qs = session.query(Network)
            for key, value in query.items():
                qs = qs.filter(getattr(Network, key) == value)
            return qs.all()
        elif isinstance(query, tuple):
            key, value = query
            return session.query(Network).filter(
                getattr(Network, key) == value).one_or_none()
        else:
            return session.query(Network).get(query)

    @classmethod
    def create(cls, user_username, name, nickname, hostname, port, realname,
               network_username, password, usermode, ssl, ssl_verify):
        """

        :param user_username: The username the network is associated with
        :param name: The name of the network to make
        :param nickname: The nickname to be used on the network
        :param hostname: The hostname of the network
        :param port: The port number
        :param realname: The User's real name for the network
        :param network_username: The username for the network
        :param password: The password for the network
        :param usermode: The user's usermode for the network
        :param ssl:
        :param ssl_verify: Bool determining is we check the ssl for the network
        :return: Network object
        """
        user_obj = session.query(User).filter(
            User.username == user_username).first()
        if user_obj is None:
            raise Exception("User is none")
        network = Network(
            name=name, nickname=nickname, hostname=hostname,
            port=port, realname=realname, username=network_username,
            password=password, usermode=usermode, ssl=ssl,
            ssl_verify=ssl_verify, user_id=user_obj.id
        )
        session.add(network)
        session.commit()
        return network

    @classmethod
    def update(cls, filter, update=None):
        if update is None:
            update = {}
        network = session.query(Network).filter(
            getattr(Network, filter[0]) == filter[1]).one()
        for key, value in update.items():
            setattr(network, key, value)
        session.add(network)
        session.commit()
        return network
