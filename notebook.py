#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Author: Seth Brown
Description: Notebook generation code
"""

import os
import sys
import qrcode
import datetime

def ref_file(page_stamp, img_path='/Users/sbrown/Desktop/'):
    img_dir = '/images/'
    date = datetime.datetime.today().strftime('%Y-%m-%d-')
    img = ''.join((page_stamp, '.png'))
    fill = ('---', 'author: Seth Brown', 'layout: post',
            'title: "{0}"'.format(page_stamp),
            'date: ' + date.rstrip('-'), 'categories: []',
           '---', '', '',
    '<a href="{0}{1}"><img class=centered src="{0}{1}" width="600" /></a>'.\
        format(img_dir, img))

    fill = '\n'.join(line for line in fill)

    return fill

def support_files(date, page_stamp, path='/Users/sbrown/Desktop/'):

    mkd_file = ''.join((path, date, page_stamp, '.md'))

    if not os.path.isfile(mkd_file):
        with open(mkd_file, mode='w') as outfile:
            fill = ref_file(page_stamp, path)
            outfile.write(fill)

def preface(vol_no):
    # the date the notebook was created
    est_date = datetime.date.today().strftime('%B %Y')
    preamble = (r'\documentclass{article}',
                r'\usepackage[paperheight=9.5in,paperwidth=7.31in]{geometry}',
                r'\pagestyle{empty}',
                r'\usepackage{wallpaper}',
                r'\usepackage{fontspec}',
                r'\usepackage{background}',
                r'\setromanfont{GaramondNo8}',
                r'\SetBgScale{1}',
                r'\SetBgAngle{0}',
                r'\SetBgColor{black}',
                r'\SetBgOpacity{1}',
                r'\SetBgPosition{current page.south}',
                r'\begin{document}',
                r'\vspace*{3cm}',
                r'\NoBgThispage',
                r'\centering',
                r'\begin{Huge}',
                r'\textbf{\emph{Vol. ' + str(vol_no) + r'}}',
                r'\end{Huge}\\',
                r'\vspace{0.1cm}',
                r'\textbf{\emph{' + est_date + r'}}\\',
                r'\vspace{1cm}',
                r'\begin{huge}',
                r'Seth Brown',
                r'\end{huge}\\',
                r'\vspace{0.1cm}',
                r'sethbrown@drbunsen.org \\',
                r'\vspace{10cm}',
                r'\newpage',
                r'\section*{Table of Contents}',
                r'\vspace{3cm}',
                r'\centering',
                '\n')

    return '\n'.join(i for i in preamble)

def page_stamps(bookno, page_end=500):
    pages = xrange(0, page_end)
    stamps = (''.join((str(bookno), '-', str(page))) for page in pages)

    return [stamp for stamp in stamps]

def toc_lines(stamps):
    dots = '.' * 100
    eol = r'\\'

    return ''.join('{0:<10}{1}{2}\n'.format(stamp, dots, eol)
            for stamp in stamps)

def qr(date, page_stamp):
    qr_handle = ''.join(('qr_', page_stamp, '.png'))
    img_link = ''.join(('nebulous://notebook/', date, page_stamp, '.md'))
    img = qrcode.make(img_link)
    img.save(qr_handle)

    return qr_handle

def notepage(page_stamp, qr_handle):
    page = (r'\newpage',
            r'\mbox{}',
            r'\CenterWallPaper{1.02}{notebook.eps}',
            r'\SetBgVshift{0.5cm}',
            r'\SetBgContents{' + page_stamp + r'}',
            r'\LLCornerWallPaper{0.09}{' + qr_handle + '}')

    return '\n'.join(i for i in page)

def end():
    return  '\n'.join((r'\newpage', '\n', r'\end{document}'))

def main(vol, pages):
    vol = int(vol)
    pages = int(pages)
    date = datetime.datetime.today().strftime('%Y-%m-%d-')

    stamps = page_stamps(vol, pages)
    [support_files(date, stamp) for stamp in stamps]

    with open('notebook.tex', mode='w') as outfile:
        p = preface(vol)
        t = toc_lines(stamps)
        a = p + t
        outfile.write(a)
        for stamp in stamps:
            q = qr(date, stamp)
            n = notepage(stamp, q)
            outfile.write(n)
        e = end()
        outfile.write(e)

if __name__ == '__main__':
    main(13, 100)
