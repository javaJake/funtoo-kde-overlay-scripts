#!/usr/bin/python3

import os
from merge_utils import *

funtoo_kde_overlay = GitTree("funtoo-kde-overlay", "master", "https://github.com/javaJake/kde", root="/home/jacob/funtoo-git/funtoo-kde-overlay", pull=False)

def kde_update():
	gentoo_kde_overlay = GitTree("gentoo-kde-overlay", "master", "https://github.com/gentoo/kde", root="/home/jacob/funtoo-git/gentoo-kde-overlay", pull=True)
	gentoo_src = GitTree("gentoo.git", "master", "https://anongit.gentoo.org/git/repo/gentoo.git", root="/home/jacob/funtoo-git/gentoo", pull=True)

	intro_steps = [
		GitCheckout("master"),
		CleanTree(),
		SyncDir("/home/jacob/kde-funtoo-scripts/kde-extras"),
	]
	import_gentoo_steps = [
		InsertEbuilds(gentoo_src, select=get_pkglist("kde-packages"), replace=True),
		InsertEclasses(gentoo_src, select=re.compile("kde.*\.eclass")),
		InsertEclasses(gentoo_src, select=re.compile("qt4-.*\.eclass")),
		InsertEclasses(gentoo_src, select=re.compile("qt5-.*\.eclass")),
	]
	import_kde_steps = [
		SyncDir(gentoo_kde_overlay.root, "Documentation", "Documentation"),
		SyncDir(gentoo_kde_overlay.root, "profiles", "profiles"),
		SyncDir(gentoo_kde_overlay.root, "metadata", "metadata"),
		InsertEbuilds(gentoo_kde_overlay, merge=True, replace=True),
		InsertEclasses(gentoo_kde_overlay),
	]
	funtoo_kde_overlay.run(intro_steps)
	funtoo_kde_overlay.run(import_gentoo_steps)
	funtoo_kde_overlay.run(import_kde_steps)
	with open("/home/jacob/funtoo-git/funtoo-kde-overlay/profiles/repo_name", "w") as f:
		f.write("funtoo-kde-overlay\n")
	funtoo_kde_overlay.gitCommit(message="automatic updates")

kde_update()

# vim: ts=4 sw=4 noet
