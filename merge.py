import os
import sqlite3


def attachStitch(a, b, dbNames, tables, conn, c):

    for index in range(a, b):
        print(index)
        current_db = dbNames[index]
        aliasDB = current_db[0: len(current_db) - 3]
        c.execute("ATTACH '{}' AS '{}';".format(dbNames[index], aliasDB))
        for tab in tables:
            query = "INSERT INTO " + str(tab) + " SELECT * FROM " + str(aliasDB) + '.' + str(tab)
            print(query)
            c.execute(query)
    conn.commit()
    conn.close()


def main():
    os.chdir('C:\\Users\\vbpr\\Desktop\\Project X\\mergeTry')

    dbNames = []
    for f in os.listdir():
        if f.find("db") != -1:
            dbNames += [f]

    conn = sqlite3.connect('{}'.format(dbNames[0]))
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite%';")
    fetchTab = c.fetchall()
    tables = [item for ft in fetchTab for item in ft]  # list of tuples into list
    print(tables)

    upCap = len(dbNames)
    for i in range(1, upCap, 10):
        diff = upCap - i
        if diff >= 10:
            attachStitch(i, i + 10, dbNames, tables, conn, c)
            conn = sqlite3.connect('{}'.format(dbNames[0]))
            c = conn.cursor()
        else:
            attachStitch(i, i + diff, dbNames, tables, conn, c)

    os.rename(r'C:\Users\vbpr\Desktop\Project X\mergeTry\exportsr_hires_1687278_20210409_144719_SAST_spcollect.db',
              r'connected.db')


if __name__ == "__main__":
    main()
