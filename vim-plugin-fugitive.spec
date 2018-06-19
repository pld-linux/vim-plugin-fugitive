%define		plugin	fugitive
Summary:	Vim plugin: A Git wrapper so awesome, it should be illegal
Name:		vim-plugin-%{plugin}
Version:	2.3
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/tpope/vim-fugitive/archive/v%{version}.tar.gz
# Source0-md5:	4e91b509b6df11adbcc2a59de19f3d34
URL:		http://majutsushi.github.com/fugitive/
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
View any blob, tree, commit, or tag in the repository with :Gedit (and
:Gsplit, :Gvsplit, :Gtabedit, ...). Edit a file in the index and write
to it to stage the changes. Use :Gdiff to bring up the staged version
of the file side by side with the working tree version and use Vim's
diff handling capabilities to stage a subset of the file's changes.

Bring up the output of git-status with :Gstatus. Press `-` to
add/reset a file's changes, or `p` to add/reset --patch. And guess
what :Gcommit does!

:Gblame brings up an interactive vertical split with git-blame output.
Press enter on a line to reblame the file as it stood in that commit,
or`o` to open that commit in a split.

:Gmove does a git-mv on a file and simultaneously renames the buffer.
:Gremove does a git-rm on a file and simultaneously deletes the
buffer.

Use :Ggrep to search the work tree (or any arbitrary commit) with
git-grep, skipping over that which is not tracked in the repository.
:Glog loads all previous revisions of a file into the quickfix list so
you can iterate over them and watch the file evolve!

:Gread is a variant of `git checkout -- filename` that operates on the
buffer rather than the filename. This means you can use `u` to undo it
and you never get any warnings about the file changing outside Vim.
:Gwrite writes to both the work tree and index versions of a file,
making it like git-add when called from a work tree file and like
git-checkout when called from the index or a blob in history.

%package doc
Summary:	Documentation for fugitive Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for fugitive Vim plugin.

%prep
%setup -qn vim-fugitive-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/fugitive.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/fugitive.txt
