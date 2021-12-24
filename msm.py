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

def start_server(args):
    print(args.__dict__)
    raise NotImplementedError()

def stop_server(args):
    print(args.__dict__)
    raise NotImplementedError()

def restart_server(args):
    stop_server(args)
    start_server(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command line utility that manages your minecraft server for you')
    subparsers = parser.add_subparsers(title='Commands', metavar='<command>')
    
    server_info_parser = argparse.ArgumentParser(add_help=False)
    server_info_parser.add_argument('name', help='The name of the server')

    # add server parser stuff
    add_server_parser = subparsers.add_parser('create-server', aliases=['cs'], parents=[server_info_parser], help='Creates a server')
    add_server_parser.set_defaults(func=create_server)
    add_server_parser.add_argument('-j', '--jar', help='The server jar to use when building the server')
    add_server_parser.add_argument('-t', '--server-type', choices=['vanilla', 'bukkit', 'spigot', 'paper'], default='paper', help='The type of server to use when building a jar, defaults to paper')
    add_server_parser.add_argument('-v', '--mc-version', default='latest', help='The version of minecraft to use for the server')
    add_server_parser.add_argument('-b', '--build-number', default='latest', help='specify the build number if a particular build is wanted, defaults to latest')
    
    # list servers parser stuff
    subparsers.add_parser('list-servers', aliases=['ls'], help='Lists the existing minecraft servers').set_defaults(func=list_servers)
    
    # remove server parser stuff
    subparsers.add_parser('remove', parents=[server_info_parser], help='Removes a server').set_defaults(func=remove_server)   

    # start server parser stuff
    subparsers.add_parser('start', parents=[server_info_parser], help='Starts a server').set_defaults(func=start_server)
    
    # stop server parser stuff
    subparsers.add_parser('stop', parents=[server_info_parser], help='Stops a server').set_defaults(func=stop_server)

    # restart server parser stuff

    subparsers.add_parser('restart', parents=[server_info_parser], help='Restarts a server').set_defaults(func=restart_server)


    args = parser.parse_args()
    args.func(args)


