team = []
relation_list = [["刘备", "关羽"],
                 ["刘备", "张飞"],
                 ["张飞", "诸葛亮"],
                 ["曹操", "司马懿"],
                 ["司马懿", "张辽"],
                 ["曹操", "曹丕"],
                 ["夏侯惇","曹操"],
                 ["张辽","文良"],
                 ["孙策","小乔"]]


def re_team(re_list):
    for list in re_list:
        team_index = find_team(list)
        if team_index is False:
            team.append(list)
        else:
            add_pepole(team_index,list)


def add_pepole(team_index,list3):
    for b in list3:
        if b not in team[team_index]:
            team[team_index].append(b)

            return


def find_team(list):
    for team_list in team:
        for a in list:
            if a in team_list:
                return team.index(team_list)

    else:
        return False
        pass


re_team(relation_list)
print(team)


