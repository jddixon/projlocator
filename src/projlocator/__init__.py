# projlocator/projlocator/loc.py

""" Utilities for managing a projects directory organized by language. """

import os
import shutil

__all__ = ['__version__', '__version_date__',
           # CONSTANTS
           'DEV_BASE', 'SHAREDEV_APP_DIR',
           'GH_PAGES_BASE',
           'PROJ_LIST_MAP',
           # FUNCTIONS
           'add_to_proj_list', 'drop_from_proj_list',
           'get_dir_for_lang', 'get_gh_pages_base', 'get_gh_pages_proj',
           'get_lang_for_dir', 'get_lang_for_project',
           'get_proj_defaults', 'get_proj_names',
           'proj_dir_from_name', 'proj_rel_path_from_name',
           ]

# -- exported constants ---------------------------------------------

__version__ = '0.0.7'
__version_date__ = '2017-09-16'

DEV_BASE = os.path.join(os.environ['HOME'], 'dev')
SHAREDEV_APP_DIR = '/var/app/sharedev'
GH_PAGES_BASE = os.path.join(DEV_BASE, 'gh-pages', 'projects')

# -- pseudo constant(s) ---------------------------------------------
PROJ_LIST_FILE = os.path.join(SHAREDEV_APP_DIR, 'projList')
PROJ_LIST_MAP = {}


def _update_proj_list():
    # DEBUG
    # print("entering updateProjList()")
    # END
    global PROJ_LIST_MAP
    PROJ_LIST_MAP = {}
    with open(PROJ_LIST_FILE, 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line:
                parts = line.split()
                PROJ_LIST_MAP[parts[0]] = parts[1]
            line = file.readline()

        # DEBUG
        # print("there are %d items in the map" % len(PROJ_LIST_MAP))
        # END
_update_proj_list()

# -- exported functions ---------------------------------------------


def add_to_proj_list(project, rel_path=None):
    """
    If the project does not already exist and if its relPath is not
    predictable from the project name, add it to the list in
    SHAREDEV_APP_DIR/projList.

    Raises a RuntimeError if a problem is encountered.  Otherwise
    returns the value of relPath used (ie, appended to projList).
    """
    if not project:
        raise RuntimeError('you must supply a project name!')

    if project in PROJ_LIST_MAP:
        raise RuntimeError("'%s' is already in the project list" % project)

    expected_rel_path = ''
    if project.endswith('_c'):
        expected_rel_path = os.path.join('c', project)
    elif project.endswith('_cpp'):
        expected_rel_path = os.path.join('cpp', project)
    elif project.endswith('_go'):
        expected_rel_path = os.path.join('go', 'src', 'github.com',
                                         'jddixon', project)
    elif project.endswith('_java'):
        expected_rel_path = os.path.join('java', project)
    elif project.endswith('_ml'):
        expected_rel_path = os.path.join('ml', project)
    elif project.endswith('_py'):
        expected_rel_path = os.path.join('py', project)
    elif project.endswith('_rb'):
        expected_rel_path = os.path.join('rb', project)

    if expected_rel_path:
        if rel_path:
            if rel_path != expected_rel_path:
                raise RuntimeError("relPath is '%s' but expected '%s'" % (
                    rel_path, expected_rel_path))
        else:
            rel_path = expected_rel_path
        # regular project name, so we don't update the relPath file
        return rel_path

    if not rel_path:
        raise RuntimeError(
            "'%s' is not a regular project name; you must specify a relPath" %
            project)

    tmp_file = PROJ_LIST_FILE + '.tmp'
    bak_file = PROJ_LIST_FILE + '.bak'
    shutil.copyfile(PROJ_LIST_FILE, tmp_file)
    with open(tmp_file, 'a') as file:
        file.write(project + '\t' + rel_path + '\n')

    # quasi-atomic file update
    os.rename(PROJ_LIST_FILE, bak_file)
    os.rename(tmp_file, PROJ_LIST_FILE)

    _update_proj_list()

    return rel_path


def drop_from_proj_list(project):
    """ Drop the project named from the project list. """

    if not project:
        return
    if project in PROJ_LIST_MAP:
        # DEBUG
        print("dropping project '%s'" % project)
        # END
        tmp_file = PROJ_LIST_FILE + '.tmp'
        bak_file = PROJ_LIST_FILE + '.bak'

        with open(PROJ_LIST_FILE, 'r') as file:
            data_in = file.read()
        lines = data_in.split('\n')
        if len(lines[-1]) == 0:
            lines = lines[0:-1]
        output = []
        for line in lines:
            proj, _ = line.split()     # _ was r
            if proj != project:
                output.append(line)
        data_out = '\n'.join(output) + '\n'
        # DEBUG
        print("updated projList:")
        print(data_out)              # prints an extra line :-}
        # END
        with open(tmp_file, 'w') as file:
            file.write(data_out)

        # quasi-atomic file update
        os.rename(PROJ_LIST_FILE, bak_file)
        os.rename(tmp_file, PROJ_LIST_FILE)

        _update_proj_list()
    else:
        print("the project you are trying to drop, '%s', does not exist" %
              project)


def get_gh_pages_base():
    """ Return path to gh-pages subdirectory. """
    return os.path.join(os.environ['DEV_BASE'], 'gh-pages')


def get_gh_pages_proj():
    """ Return path to gh-pages/projects subdirectory. """
    return os.path.join(get_gh_pages_base(), 'projects')


def get_proj_names():
    """ get a sorted list of all projects in gh-pages"""

    names = []
    files = os.listdir(GH_PAGES_BASE)
    if len(files) > 0:
        files.sort()
        for file in files:
            proj_dir = proj_dir_from_name(file)
            if proj_dir == "":
                continue
            names.append(file)
    return names


def proj_dir_from_name(project):
    """ get path to project directory from name """
    proj_dir = ''
    if project == "testing":
        proj_dir = "/home/jdd/dev/py/wrap_gh_page"
    else:
        rel_path = proj_rel_path_from_name(project)
        if rel_path:
            proj_dir = os.path.join(DEV_BASE, rel_path)
    return proj_dir


def proj_rel_path_from_name(project):
    """
    Get relative path from base directory (dev/ or sharedev/) to
    project directory.
    """
    if (not project) or len(project) == 0:
        raise "no project name specified"

    rel_path = ""

    # IRREGULAR PROJECT NAMES ---------------------------------------
    if project in PROJ_LIST_MAP:
        rel_path = PROJ_LIST_MAP[project]

    # PROJECT NAMES WITH STANDARD SUFFIXES --------------------------
    # If you update this, update addToProjList() as well
    elif project.endswith('_c'):
        rel_path = os.path.join('c', project)
    elif project.endswith('_cpp'):
        rel_path = os.path.join('cpp', project)
    elif project.endswith('_data'):
        rel_path = os.path.join('dat', project)
    elif project.endswith('_go'):
        rel_path = os.path.join('go', 'src', 'github.com', 'jddixon', project)
    elif project.endswith('_java'):
        rel_path = os.path.join('java', project)
    elif project.endswith('_ml'):
        rel_path = os.path.join('ml', project)
    elif project.endswith('_py'):
        rel_path = os.path.join('py', project)
    elif project.endswith('_rb'):
        rel_path = os.path.join('rb', project)
    return rel_path


# -- lang/dir pairs -------------------------------------------------
PAIRS = [\
    # to simplify searching, all paths should be slash-terminated
    ['c', os.path.join(DEV_BASE, 'c/')],
    ['cpp', os.path.join(DEV_BASE, 'cpp/')],
    ['dat', os.path.join(DEV_BASE, 'dat/')],
    ['G', os.path.join(DEV_BASE, 'gh-pages', 'projects/')],
    ['go', os.path.join(DEV_BASE, 'go', 'src', 'github.com', 'jddixon/')],
    ['java', os.path.join(DEV_BASE, 'java/')],
    ['js', os.path.join(DEV_BASE, 'node/')],
    ['py', os.path.join(DEV_BASE, 'py/')],
    ['ml', os.path.join(DEV_BASE, 'ml/')],
    ['rb', os.path.join(DEV_BASE, 'rb/')],

    # dummy language
    ['top', DEV_BASE + '/'], ]
DIR2LANG = {}
LANG2DIR = {}
for pair_ in PAIRS:
    lang_ = pair_[0]
    dir_ = pair_[1]
    DIR2LANG[dir_] = lang_
    LANG2DIR[lang_] = dir_

# -- utility functions ----------------------------------------------


def get_lang_for_project(project):
    """
    Given a project name, return the language.

    ridiculously inefficient"""

    lang = ''
    abs_path = proj_dir_from_name(project)
    if abs_path:
        lang, _, _ = get_proj_defaults(abs_path)     # was _p, _r
    return lang


def get_proj_defaults(abs_path=None):
    """
    Given the absolute path , or the current directory if no path is
    specified, return the language code, project name, and relative path
    from the project directory.  If these cannot be resolved, return None
    in all cases.
    """

    if not abs_path:
        abs_path = os.getcwd()
    lang, project, rel_path = None, None, None
    failed = True
    for pair in PAIRS:
        lang_dir = pair[1]
        if abs_path.startswith(lang_dir):
            lang = pair[0]
            failed = False
            break
    if not failed:
        len_lang_dir = len(lang_dir)
        rest_of_path = abs_path[len_lang_dir:]
        project, beep, rel_path = rest_of_path.partition('/')
        if beep != '/':
            rel_path = './'

    if failed:
        return None, None, None
    else:
        return lang, project, rel_path


def get_dir_for_lang(lang):
    """
    Given a language code, returns the corresponding absolute path without
    any trailing slash, or None.
    """
    try:
        dir_name = LANG2DIR[lang]
    except KeyError:
        dir_name = None
    return dir_name


def get_lang_for_dir(dir_name):
    """
    Given an absolute path, returns the corresponding language code or
    None if there isn't one.
    """
    if dir_name is None:
        raise RuntimeError('path may not be empty')
    if not dir_name.startswith('/'):
        raise RuntimeError('path must be absolute')
    if not dir_name.endswith('/'):
        dir_name += '/'
    try:
        lang = DIR2LANG[dir_name]
    except KeyError:
        lang = None
    return lang
