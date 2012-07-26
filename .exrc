if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <S-Tab> =BackwardsSnippet()
snoremap <silent> 	 i<Right>=TriggerSnippet()
nmap  :JavaBrowser
map  :WMToggle
snoremap  b<BS>
nmap d :cs find d =expand("<cword>")	
nmap i :cs find i ^=expand("<cfile>")$
nmap f :cs find f =expand("<cfile>")	
nmap e :cs find e =expand("<cword>")	
nmap t :cs find t =expand("<cword>")	
nmap c :cs find c =expand("<cword>")	
nmap g :cs find g =expand("<cword>")	
nmap s :cs find s =expand("<cword>")	
map   /
vnoremap $/ `>a*/`<i/*
vnoremap $< `>a -->`<i<!-- 
vnoremap $w `>a"`<i"
vnoremap $q `>a'`<i'
vnoremap $$ `>a"`<i"
vnoremap $3 `>a}`<i{
vnoremap $2 `>a]`<i[
vnoremap $1 `>a)`<i(
snoremap % b<BS>%
snoremap ' b<BS>'
nmap <silent> ,cv <Plug>VCSVimDiff
nmap <silent> ,cu <Plug>VCSUpdate
nmap <silent> ,cU <Plug>VCSUnlock
nmap <silent> ,cs <Plug>VCSStatus
nmap <silent> ,cr <Plug>VCSReview
nmap <silent> ,cq <Plug>VCSRevert
nmap <silent> ,cn <Plug>VCSAnnotate
nmap <silent> ,cN <Plug>VCSSplitAnnotate
nmap <silent> ,cl <Plug>VCSLog
nmap <silent> ,cL <Plug>VCSLock
nmap <silent> ,ci <Plug>VCSInfo
nmap <silent> ,cg <Plug>VCSGotoOriginal
nmap <silent> ,cG <Plug>VCSClearAndGotoOriginal
nmap <silent> ,cD <Plug>VCSDelete
nmap <silent> ,cc <Plug>VCSCommit
nmap <silent> ,ca <Plug>VCSAdd
nnoremap <silent> ,b :CommandTBuffer
nnoremap <silent> ,t :CommandT
nmap ,caL <Plug>CalendarH
nmap ,cal <Plug>CalendarV
nmap ,scp <Plug>SQLUCreateProcedure
nmap ,scdt <Plug>SQLUGetColumnDataType
nmap ,scd <Plug>SQLUGetColumnDef
nmap ,scl <Plug>SQLUCreateColumnList
vmap ,sf <Plug>SQLUFormatter
nmap ,sf <Plug>SQLUFormatter
vmap ,sfs <Plug>SQLUFormatter
nmap ,sfs <Plug>SQLUFormatter
vmap ,sfr <Plug>SQLUFormatStmts
nmap ,sfr <Plug>SQLUFormatStmts
noremap ,vcs :e res/values-zh-rCN/strings.xml
noremap ,ves :e res/values/strings.xml
noremap ,di :call DebugInnerContacts()
noremap ,dd :call StartDebug()
noremap ,tc :!adb_connect
noremap ,tr :!adb_connect&&adb shell stop && adb shell start
nnoremap ,0 :10b
nnoremap ,9 :9b
nnoremap ,8 :8b
nnoremap ,7 :7b
nnoremap ,6 :6b
nnoremap ,5 :5b
nnoremap ,4 :4b
nnoremap ,3 :3b
map ,z <Plug>ZoomWin
noremap <silent> ,bc :!find -name *.java > cscope.files && cscope -b -q
noremap ,ts :!target_sync
map ,s :so ~/.vimrc
map ,v :e ~/.vimrc
map <silent> ,vp :!xdg-open %
map ,ac :!adb_connect&&adb logcat -c
map ,al :!adb_connect&&adb logcat
map ,vxs :sp ~/.vim/snippets/xml.snippets
map ,vjs :sp ~/.vim/snippets/java.snippets
nmap ,rr :call ReloadSnippets(snippets_dir, &filetype)
noremap ,m :%s/\r//g
map ,y :YRShow
map ,s? z=
map ,sa zg
map ,sp [
map ,sn ]
map ,q :e ~/buffer
map ,cd :cd %:p:h
nmap ,fu :se ff=unix
nmap ,fd :se ff=dos
map ,$ :syntax sync fromstart
vmap ,4 :set ft=javascript
omap ,4 :set ft=javascript
vmap ,3 :set syntax=python
omap ,3 :set syntax=python
map ,2 :set syntax=xhtml
map ,1 :set syntax=cheetah
nmap ,w :w!
nmap ,x :xa!
map 0 ^
snoremap U b<BS>U
vmap [% [%m'gv``
snoremap \ b<BS>\
vmap ]% ]%m'gv``
snoremap ^ b<BS>^
snoremap ` b<BS>`
vmap a% [%v]%
nmap gx <Plug>NetrwBrowseX
snoremap <Left> bi
snoremap <Right> a
snoremap <BS> b<BS>
snoremap <silent> <S-Tab> i<Right>=BackwardsSnippet()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
nnoremap <silent> <Plug>VCSVimDiff :VCSVimDiff
nnoremap <silent> <Plug>VCSUpdate :VCSUpdate
nnoremap <silent> <Plug>VCSUnlock :VCSUnlock
nnoremap <silent> <Plug>VCSStatus :VCSStatus
nnoremap <silent> <Plug>VCSSplitAnnotate :VCSAnnotate!
nnoremap <silent> <Plug>VCSReview :VCSReview
nnoremap <silent> <Plug>VCSRevert :VCSRevert
nnoremap <silent> <Plug>VCSLog :VCSLog
nnoremap <silent> <Plug>VCSLock :VCSLock
nnoremap <silent> <Plug>VCSInfo :VCSInfo
nnoremap <silent> <Plug>VCSClearAndGotoOriginal :VCSGotoOriginal!
nnoremap <silent> <Plug>VCSGotoOriginal :VCSGotoOriginal
nnoremap <silent> <Plug>VCSDiff :VCSDiff
nnoremap <silent> <Plug>VCSDelete :VCSDelete
nnoremap <silent> <Plug>VCSCommit :VCSCommit
nnoremap <silent> <Plug>VCSAnnotate :VCSAnnotate
nnoremap <silent> <Plug>VCSAdd :VCSAdd
nmap <Nul><Nul>d :vert scs find d =expand("<cword>")
nmap <Nul><Nul>i :vert scs find i ^=expand("<cfile>")$	
nmap <Nul><Nul>f :vert scs find f =expand("<cfile>")	
nmap <Nul><Nul>e :vert scs find e =expand("<cword>")
nmap <Nul><Nul>t :vert scs find t =expand("<cword>")
nmap <Nul><Nul>c :vert scs find c =expand("<cword>")
nmap <Nul><Nul>g :vert scs find g =expand("<cword>")
nmap <Nul><Nul>s :vert scs find s =expand("<cword>")
nmap <Nul>d :scs find d =expand("<cword>")	
nmap <Nul>i :scs find i ^=expand("<cfile>")$	
nmap <Nul>f :scs find f =expand("<cfile>")	
nmap <Nul>e :scs find e =expand("<cword>")	
nmap <Nul>t :scs find t =expand("<cword>")	
nmap <Nul>c :scs find c =expand("<cword>")	
nmap <Nul>g :scs find g =expand("<cword>")	
nmap <Nul>s :scs find s =expand("<cword>")	
nnoremap <silent> <F11> :call conque_term#exec_file()
nnoremap <silent> <Plug>CalendarH :cal Calendar(1)
nnoremap <silent> <Plug>CalendarV :cal Calendar(0)
map <F2> :NERDTreeToggle
map <silent> <F5> :!ctags -R --language-force=java --exclude=\.* 
map <F3> :Tlist
map <F9> ggVGg?
cnoremap  <Home>
cnoremap  <End>
inoremap <silent> 	 =TriggerSnippet()
cnoremap  
inoremap <silent> 	 =ShowAvailableSnips()
cnoremap $td tabnew ~/Desktop/
cnoremap $th tabnew ~/
vmap ë :m'<-2`>my`<mzgv`yo`z
vmap ê :m'>+`<my`>mzgv`yo`z
nmap ë mz:m-2`z
nmap ê mz:m+`z
cabbr <expr> %$ expand('%:t:r')
cabbr <expr> %% expand('%:h')
iabbr xdate =strftime("%d/%m/%y %H:%M:%S")
let &cpo=s:cpo_save
unlet s:cpo_save
set ambiwidth=double
set autoindent
set autoread
set autowrite
set background=dark
set backspace=2
set cindent
set cmdheight=2
set cscopeverbose
set expandtab
set fileencodings=ucs-bom,utf-8,cp936,big5,euc-jp,euc-kr,latin1
set fileformats=unix,dos,mac
set hidden
set history=400
set ignorecase
set incsearch
set laststatus=2
set lazyredraw
set makeprg=mm
set matchtime=8
set modelines=0
set mouse=a
set path=.,/usr/include,,,res/layout,res/layout-finger,res/values,res/drawable,res/drawable-mdpi
set ruler
set scrolloff=7
set sessionoptions=options
set shell=bash\ -l
set shiftwidth=4
set showmatch
set smartindent
set smarttab
set softtabstop=4
set statusline=%02n:%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %P
set suffixesadd=.java,.xml,.9.png,.png
set noswapfile
set tabline=%!TabCaptionLineFunction()
set viminfo='10,
set whichwrap=b,s,<,>,h,l
set wildmenu
set window=0
set nowritebackup
" vim: set ft=vim :
