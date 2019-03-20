#pragma once

typedef struct bot
{
	char serialNumber[40];
	char state[40];
	char specialization[40];
	int energyCostToRepair;
}bot;

typedef struct list
{
	bot bots[1001];
	int lengthOfTheList ;
}list;

list botRepository;

void initRepository()
{
	botRepository.lengthOfTheList = 0;
}