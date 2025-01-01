import React, { useState } from 'react';
import { Card, Select, Typography, Row, Col, Space } from 'antd';
import { CalendarOutlined, EnvironmentOutlined, TeamOutlined } from '@ant-design/icons';
import FixtureCard from '../components/FixtureCard';

const { Title } = Typography;

const FixturesPage = () => {
    const [selectedCompetition, setSelectedCompetition] = useState('all');

    // Sample fixtures data - replace with actual data
    const fixtures = [
        {
            id: 1,
            competition: 'Premier League',
            date: '2024-01-30',
            homeTeam: 'Manchester City',
            awayTeam: 'Liverpool',
            time: '20:00',
            venue: 'Etihad Stadium',
            attendance: 53000,
            haalandPlayed: true,
            haalandGoals: 2,
            haalandAssists: 1
        },
        // Add more fixtures
    ];

    const competitions = [
        { value: 'all', label: 'All Competitions' },
        { value: 'premier-league', label: 'Premier League' },
        { value: 'champions-league', label: 'Champions League' },
        { value: 'fa-cup', label: 'FA Cup' },
    ];

    const filteredFixtures = selectedCompetition === 'all'
        ? fixtures
        : fixtures.filter(fixture => fixture.competition.toLowerCase().replace(' ', '-') === selectedCompetition);

    return (
        <div style={{ maxWidth: 1200, margin: '0 auto', padding: '32px 16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 32 }}>
                <Title level={2}>Fixtures</Title>

                <Space>
                    <Select
                        value={selectedCompetition}
                        onChange={setSelectedCompetition}
                        options={competitions}
                        style={{ width: 200 }}
                    />
                </Space>
            </div>

            {/* Upcoming Fixtures */}
            <div style={{ marginBottom: 32 }}>
                <Title level={3}>Upcoming Fixtures</Title>
                <Row gutter={[24, 24]}>
                    {filteredFixtures.filter(fixture => new Date(fixture.date) > new Date()).map(fixture => (
                        <Col xs={24} md={12} lg={8} key={fixture.id}>
                            <FixtureCard fixture={fixture} />
                        </Col>
                    ))}
                </Row>
            </div>

            {/* Past Results */}
            <div style={{ marginBottom: 32 }}>
                <Title level={3}>Recent Results</Title>
                <Row gutter={[24, 24]}>
                    {filteredFixtures.filter(fixture => new Date(fixture.date) <= new Date()).map(fixture => (
                        <Col xs={24} md={12} lg={8} key={fixture.id}>
                            <FixtureCard fixture={fixture} />
                        </Col>
                    ))}
                </Row>
            </div>

            {/* Competition Summary */}
            <div>
                <Title level={3}>Competition Summary</Title>
                <Row gutter={[24, 24]}>
                    <Col xs={24} md={8}>
                        <CompetitionSummaryCard
                            competition="Premier League"
                            played={20}
                            won={15}
                            drawn={3}
                            lost={2}
                        />
                    </Col>
                    <Col xs={24} md={8}>
                        <CompetitionSummaryCard
                            competition="Champions League"
                            played={6}
                            won={5}
                            drawn={1}
                            lost={0}
                        />
                    </Col>
                    <Col xs={24} md={8}>
                        <CompetitionSummaryCard
                            competition="FA Cup"
                            played={2}
                            won={2}
                            drawn={0}
                            lost={0}
                        />
                    </Col>
                </Row>
            </div>
        </div>
    );
};

const CompetitionSummaryCard = ({ competition, played, won, drawn, lost }) => (
    <Card>
        <Title level={4} style={{ marginBottom: 16 }}>{competition}</Title>
        <Row gutter={[16, 16]}>
            <Col span={12}>
                <div>
                    <Typography.Text type="secondary">Played</Typography.Text>
                    <div style={{ fontSize: 24, fontWeight: 'bold' }}>{played}</div>
                </div>
            </Col>
            <Col span={12}>
                <div>
                    <Typography.Text type="secondary">Won</Typography.Text>
                    <div style={{ fontSize: 24, fontWeight: 'bold', color: '#52c41a' }}>{won}</div>
                </div>
            </Col>
            <Col span={12}>
                <div>
                    <Typography.Text type="secondary">Drawn</Typography.Text>
                    <div style={{ fontSize: 24, fontWeight: 'bold', color: '#faad14' }}>{drawn}</div>
                </div>
            </Col>
            <Col span={12}>
                <div>
                    <Typography.Text type="secondary">Lost</Typography.Text>
                    <div style={{ fontSize: 24, fontWeight: 'bold', color: '#f5222d' }}>{lost}</div>
                </div>
            </Col>
        </Row>
    </Card>
);

export default FixturesPage;