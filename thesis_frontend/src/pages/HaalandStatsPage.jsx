import React from 'react';
import { Card, Row, Col, Statistic, Typography, List } from 'antd';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { TrophyOutlined, ClockCircleOutlined, ThunderboltOutlined, AimOutlined } from '@ant-design/icons';
import ShotMap from '../components/ShotMap';

const { Title, Text } = Typography;

const HaalandPage = () => {
    // Sample data - replace with actual data
    const performanceData = [
        { month: 'Aug', goals: 5, assists: 2, xG: 4.2 },
        { month: 'Sep', goals: 6, assists: 1, xG: 5.8 },
        { month: 'Oct', goals: 4, assists: 3, xG: 3.9 },
        { month: 'Nov', goals: 5, assists: 2, xG: 4.5 },
        { month: 'Dec', goals: 5, assists: 0, xG: 4.8 },
    ];

    const shotData = [
        // Add shot data for the shot map
    ];

    return (
        <div className="container">
            <Title level={1} className="mb-8">Haaland Statistics</Title>

            {/* Key Stats */}
            <Row gutter={[16, 16]} className="mb-8">
                <StatCard
                    title="Total Goals"
                    value="25"
                    subtitle="This Season"
                    icon={<AimOutlined style={{ fontSize: '24px', color: '#1677ff' }} />}
                />
                <StatCard
                    title="Assists"
                    value="8"
                    subtitle="This Season"
                    icon={<TrophyOutlined style={{ fontSize: '24px', color: '#52c41a' }} />}
                />
                <StatCard
                    title="Minutes Played"
                    value="2,250"
                    subtitle="This Season"
                    icon={<ClockCircleOutlined style={{ fontSize: '24px', color: '#722ed1' }} />}
                />
                <StatCard
                    title="Goals per 90"
                    value="1.2"
                    subtitle="This Season"
                    icon={<ThunderboltOutlined style={{ fontSize: '24px', color: '#faad14' }} />}
                />
            </Row>

            {/* Performance Chart */}
            <Card title="Performance Over Time" bordered={false} className="mb-8">
                <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={performanceData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="month" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="goals" stroke="#1677ff" name="Goals" />
                        <Line type="monotone" dataKey="xG" stroke="#93c5fd" name="Expected Goals" strokeDasharray="5 5" />
                        <Line type="monotone" dataKey="assists" stroke="#52c41a" name="Assists" />
                    </LineChart>
                </ResponsiveContainer>
            </Card>

            {/* Shot Map */}
            <Card title="Shot Map" bordered={false} className="mb-8">
                <ShotMap shots={shotData} />
            </Card>

            {/* Detailed Stats */}
            <Row gutter={[16, 16]}>
                <Col xs={24} md={12} lg={8}>
                    <DetailedStatsCard
                        title="Shooting Stats"
                        stats={[
                            { label: 'Total Shots', value: '89' },
                            { label: 'Shots on Target', value: '45' },
                            { label: 'Shot Accuracy', value: '50.6%' },
                            { label: 'Goals per Shot', value: '0.28' },
                            { label: 'Expected Goals (xG)', value: '22.5' },
                            { label: 'Goals - xG', value: '+2.5' },
                        ]}
                    />
                </Col>
                <Col xs={24} md={12} lg={8}>
                    <DetailedStatsCard
                        title="General Stats"
                        stats={[
                            { label: 'Games Played', value: '25' },
                            { label: 'Minutes per Goal', value: '90' },
                            { label: 'Assists', value: '8' },
                            { label: 'Penalties Scored', value: '5/6' },
                            { label: 'Headers', value: '6' },
                            { label: 'Through Balls', value: '15' },
                        ]}
                    />
                </Col>
            </Row>
        </div>
    );
};

const StatCard = ({ title, value, subtitle, icon }) => (
    <Col xs={24} sm={12} lg={6}>
        <Card bordered={false}>
            <Row justify="space-between" align="middle">
                <Col>{icon}</Col>
                <Col>
                    <Statistic title={title} value={value} />
                    <Text type="secondary">{subtitle}</Text>
                </Col>
            </Row>
        </Card>
    </Col>
);

const DetailedStatsCard = ({ title, stats }) => (
    <Card title={title} bordered={false}>
        <List
            itemLayout="horizontal"
            dataSource={stats}
            renderItem={(item) => (
                <List.Item>
                    <List.Item.Meta title={item.label} />
                    <Text strong>{item.value}</Text>
                </List.Item>
            )}
        />
    </Card>
);

export default HaalandPage;
