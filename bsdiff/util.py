import commands


def bsdiff(oldfile, newfile, patchfile):
    cmd = 'bsdiff %s %s %s' % (oldfile, newfile, patchfile)
    return commands.getoutput(cmd)
