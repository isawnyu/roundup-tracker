# Copyright (c) 2011 cwarner@kernelcode.com (http://cwarner.kernelcode.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
from roundup.anypy.sets_ import set
from roundup import roundupdb, hyperdb

def deptissue(db, cl, nodeid, oldvalues):

    # get all message info
    create = cl.generateCreateNote(nodeid)
    dept_id = cl.get(nodeid, 'department')
    print dept_id

    ''' BUILDING DEPARTMENT '''
    # You have to know the id mapping
    #  technically we could find this

    if dept_id == '1':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Building Engineering Department"
                cl.send_message(nodeid, msgid, create, ['mike.kojasevic@leonlevy.org'])
                cl.send_message(nodeid, msgid, create, ['diane.bennett@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

    elif dept_id == '2':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Technology Department"
                cl.send_message(nodeid, msgid, create, ['isaw.it@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

    elif dept_id == '3':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Research Department"
                cl.send_message(nodeid, msgid, create, ['isaw.library@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message
    else:
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Department doesn't exist"
                cl.send_message(nodeid, msgid, create, ['isaw.it@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

def init(db):
    # check on create of ticket
    db.issue.react('create', deptissue)
