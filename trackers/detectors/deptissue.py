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

    ''' BUILDING DEPARTMENT '''
    # You have to know the id mapping
    # technically we could find this

    if dept_id == '1':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Building Engineering Team"
                cl.send_message(nodeid, msgid, create, ['mike.kojasevic@leonlevy.org'])
                cl.send_message(nodeid, msgid, create, ['diane.bennett@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['tom.elliott@nyu.edu'])
                # Dwayne Boyd
                cl.send_message(nodeid, msgid, create, ['db1723@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

    elif dept_id == '2':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting IT Support Team"
                cl.send_message(nodeid, msgid, create, ['anshul.jain@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['kristen.soule@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['tom.elliott@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

    elif dept_id == '4':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Web Team"
                cl.send_message(nodeid, msgid, create, ['kristen.soule@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['tom.elliott@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

    elif dept_id == '5':
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Alerting Administrative Team"
                cl.send_message(nodeid, msgid, create, ['diane.bennett@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['roger.bagnall@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['andrea.chang@nyu.edu'])
                cl.send_message(nodeid, msgid, create, ['tom.elliott@nyu.edu'])

            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message
                
    else:
        for msgid in cl.get(nodeid, 'messages'):
            try:
                print "Department %s doesn't exist" % dept_id
                cl.send_message(nodeid, msgid, create, ['isaw.it-group@nyu.edu'])
            except roundupdb.MessageSendError, message:
                raise roundupdb.DetectorError, message

def init(db):
    # check on create of ticket
    db.issue.react('create', deptissue)
