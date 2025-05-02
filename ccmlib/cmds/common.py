from ccmlib.cmds import cluster_cmds, command, node_cmds


def get_command(kind, cmd):
    cmd_name = kind.lower().capitalize() + cmd.lower().capitalize() + "Cmd"
    try:
        klass = (cluster_cmds if kind.lower() == 'cluster' else node_cmds).__dict__[cmd_name]
    except KeyError:
        return None
    if not issubclass(klass, command.Cmd):
        return None
    return klass()
