#!/usr/bin/python3
import argparse
import re

def create_server(args):
    print(args.__dict__)
    raise NotImplementedError()

def list_servers(args):
    print(args.__dict__)
    raise NotImplementedError()

def remove_server(args):
    print(args.__dict__)
    raise NotImplementedError()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line utility that manages your minecraft server for you')
    subparsers = parser.add_subparsers(title='Commands', metavar='<command>')
    
    # add server parser stuff
    add_server_parser = subparsers.add_parser('create-server', aliases=['cs'], help='Creates a server')
    add_server_parser.set_defaults(func=create_server)
    add_server_parser.add_argument('name', help='The name of the server')
    add_server_parser.add_argument('-j', '--jar', help='The server jar to use when building the server')
    add_server_parser.add_argument('-t', '--server-type', choices=['vanilla', 'bukkit', 'spigot', 'paper'], default='paper', help='The type of server to use when building a jar, defaults to paper')
    add_server_parser.add_argument('-v', '--mc-version', default='latest', help='The version of minecraft to use for the server')
    add_server_parser.add_argument('-b', '--build-number', default='latest', help='specify the build number if a particular build is wanted, defaults to latest')
    
    # list servers parser stuff
    list_servers_parser = subparsers.add_parser('list-servers', aliases=['ls'], help='Lists the existing minecraft servers')
    list_servers_parser.set_defaults(func=list_servers)
    
    # remove server parser stuff
    remove_server_parser = subparsers.add_parser('remove-server', aliases=['rs'], help='Removes a server')
    remove_server_parser.set_defaults(func=remove_server)
    remove_server_parser.add_argument('name', help='The name of the server to delete')


    args = parser.parse_args()
    args.func(args)


