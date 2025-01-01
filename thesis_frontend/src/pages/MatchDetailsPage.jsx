import { ClockCircleOutlined, EnvironmentOutlined, TeamOutlined } from '@ant-design/icons';
import { Card, Col, Progress, Row, Typography } from 'antd';
import React from 'react';
import ShotMap from '../components/ShotMap';

const { Title, Text } = Typography;

const MatchDetailsPage = () => {
    // Sample match data - replace with actual data
    const matchData = {
        id: 1,
        competition: 'Premier League',
        date: '2024-01-30',
        homeTeam: 'Manchester City',
        awayTeam: 'Liverpool',
        score: '3-1',
        venue: 'Etihad Stadium',
        attendance: 53000,
        stats: {
            possession: { home: 65, away: 35 },
            shots: { home: 18, away: 8 },
            shotsOnTarget: { home: 8, away: 3 },
            corners: { home: 7, away: 4 },
            fouls: { home: 9, away: 12 }
        },
        events: [
            { time: '23', type: 'goal', team: 'home', player: 'Erling Haaland', assist: 'Kevin De Bruyne' },
            { time: '45+2', type: 'yellow', team: 'away', player: 'Virgil van Dijk' },
            { time: '67', type: 'goal', team: 'home', player: 'Erling Haaland', assist: 'Phil Foden' },
            { time: '78', type: 'goal', team: 'away', player: 'Mohamed Salah' },
            { time: '89', type: 'goal', team: 'home', player: 'Kevin De Bruyne' },
        ]
    };

    return (
        <div className="container">
            {/* Match Header */}
            <Card bordered={false} className="mb-8">
                <div style={{ textAlign: 'center', marginBottom: '24px' }}>
                    <Text type="secondary" style={{ fontSize: '14px', fontWeight: '500' }}>
                        {matchData.competition}
                    </Text>
                    <Row justify="center" align="middle" style={{ margin: '16px 0' }}>
                        <Col style={{ textAlign: 'center' }}>
                            <img src="/city-logo.png" alt="Man City" style={{ width: '64px', height: '64px' }} />
                            <div style={{ fontWeight: 'bold' }}>{matchData.homeTeam}</div>
                        </Col>
                        <Col>
                            <Title level={2} style={{ margin: '0 16px' }}>{matchData.score}</Title>
                        </Col>
                        <Col style={{ textAlign: 'center' }}>
                            <img src="/liverpool-logo.png" alt="Liverpool" style={{ width: '64px', height: '64px' }} />
                            <div style={{ fontWeight: 'bold' }}>{matchData.awayTeam}</div>
                        </Col>
                    </Row>
                    <Row justify="center" gutter={[16, 16]} style={{ marginTop: '16px' }}>
                        <Col>
                            <ClockCircleOutlined /> {matchData.date}
                        </Col>
                        <Col>
                            <EnvironmentOutlined /> {matchData.venue}
                        </Col>
                        <Col>
                            <TeamOutlined /> {matchData.attendance.toLocaleString()}
                        </Col>
                    </Row>
                </div>
            </Card>

            {/* Match Stats */}
            <Row gutter={16} className="mb-8">
                <Col xs={24} md={12}>
                    <Card title="Match Statistics" bordered={false}>
                        <StatBar
                            label="Possession"
                            homeValue={matchData.stats.possession.home}
                            awayValue={matchData.stats.possession.away}
                        />
                        <StatBar
                            label="Shots"
                            homeValue={matchData.stats.shots.home}
                            awayValue={matchData.stats.shots.away}
                        />
                        <StatBar
                            label="Shots on Target"
                            homeValue={matchData.stats.shotsOnTarget.home}
                            awayValue={matchData.stats.shotsOnTarget.away}
                        />
                        <StatBar
                            label="Corners"
                            homeValue={matchData.stats.corners.home}
                            awayValue={matchData.stats.corners.away}
                        />
                        <StatBar
                            label="Fouls"
                            homeValue={matchData.stats.fouls.home}
                            awayValue={matchData.stats.fouls.away}
                        />
                    </Card>
                </Col>
                <Col xs={24} md={12}>
                    <Card title="Match Timeline" bordered={false}>
                        {matchData.events.map((event, index) => (
                            <TimelineEvent key={index} event={event} />
                        ))}
                    </Card>
                </Col>
            </Row>

            {/* Shot Map */}
            <Card title="Shot Map" bordered={false}>
                <ShotMap shots={[]} /> {/* Add actual shot data */}
            </Card>
        </div>
    );
};

const StatBar = ({ label, homeValue, awayValue }) => {
    const total = homeValue + awayValue;
    const homePercentage = (homeValue / total) * 100;
    const awayPercentage = (awayValue / total) * 100;

    return (
        <div style={{ marginBottom: '16px' }}>
            <Text type="secondary">{label}</Text>
            <Row justify="space-between">
                <Text>{homeValue}</Text>
                <Text>{awayValue}</Text>
            </Row>
            <Progress
                percent={homePercentage}
                success={{ percent: homePercentage }}
                showInfo={false}
                strokeColor="#1890ff"
                trailColor="#ff4d4f"
            />
        </div>
    );
};

const TimelineEvent = ({ event }) => {
    const getEventIcon = (type) => {
        switch (type) {
            case 'goal':
                return <Text style={{ color: '#52c41a' }}>⚽</Text>;
            case 'yellow':
                return <Text style={{ backgroundColor: '#ffec3d', padding: '0 4px' }}>Yellow Card</Text>;
            case 'red':
                return <Text style={{ backgroundColor: '#ff4d4f', padding: '0 4px' }}>Red Card</Text>;
            default:
                return null;
        }
    };

    return (
        <Row gutter={16} align="middle" style={{ marginBottom: '8px' }}>
            <Col>{event.time}'</Col>
            <Col>{getEventIcon(event.type)}</Col>
            <Col>
                <Text strong>{event.player}</Text>
                {event.assist && <Text type="secondary"> (assist: {event.assist})</Text>}
            </Col>
        </Row>
    );
};

export default MatchDetailsPage;
