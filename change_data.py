# -*- coding: utf-8 -*-
# Run this script if something has changed after a draw

import cPickle as pickle
from functions import *

with open(os.path.join(LOG_FOLDER, "data-pickled"), "rb") as fp:
    db = pickle.load(fp)

# change something
for p in db.participants:
    if p.id == 26:
        p.name = u"Соколов Лев"
        p.email = "lsokolov@appliedtech.ru"
        break

with open(os.path.join(LOG_FOLDER, "data-pickled"), "wb") as fp:
    pickle.dump(db, fp)
