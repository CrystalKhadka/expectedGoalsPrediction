// Fixture Data
export const fixtures = [
    {
        id: 1,
        competition: 'Premier League',
        homeTeam: 'Manchester City',
        awayTeam: 'Arsenal',
        date: '2024-01-05',
        score: '3-1',
        haalandPlayed: true,
        haalandGoals: 2,
        haalandAssists: 1,
        venue: 'Etihad Stadium',
        attendance: 53000,
    },
    {
        id: 2,
        competition: 'Champions League',
        homeTeam: 'Manchester City',
        awayTeam: 'Real Madrid',
        date: '2024-01-12',
        score: '2-2',
        haalandPlayed: true,
        haalandGoals: 1,
        haalandAssists: 0,
        venue: 'Etihad Stadium',
        attendance: 54000,
    },
    // Add more fixtures...
];

// Shot Map Data
export const shotMapData = [
    {
        id: 1,
        matchId: 1,
        xCoord: 83,
        yCoord: 45,
        outcome: 'goal',
        minute: 23,
        xG: 0.76,
    },
    {
        id: 2,
        matchId: 1,
        xCoord: 75,
        yCoord: 32,
        outcome: 'saved',
        minute: 45,
        xG: 0.34,
    },
    // Add more shots...
];

// Haaland Performance Data
export const haalandStats = {
    totalMatches: 25,
    goals: 27,
    assists: 8,
    shotsOnTarget: 45,
    shotAccuracy: 68.5,
    xG: 24.8,
    xA: 6.5,
    minutesPlayed: 2250,
    matchesByCompetition: {
        'Premier League': 18,
        'Champions League': 5,
        'FA Cup': 2,
    },
    goalsByCompetition: {
        'Premier League': 20,
        'Champions League': 5,
        'FA Cup': 2,
    },
};

// Match Events Data
export const matchEvents = [
    {
        matchId: 1,
        events: [
            {
                minute: 23,
                type: 'goal',
                player: 'Erling Haaland',
                description: 'Goal from inside the box',
                assistedBy: 'Kevin De Bruyne',
            },
            {
                minute: 45,
                type: 'yellow_card',
                player: 'Rodri',
                description: 'Tactical foul',
            },
            // Add more events...
        ],
    },
    // Add more matches...
];