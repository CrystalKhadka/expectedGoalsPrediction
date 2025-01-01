import {
  AimOutlined,
  CalendarOutlined,
  TrophyOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Card, Col, Row, Statistic } from 'antd';
import React from 'react';

const HomePage = () => {
  return (
    <div className='container mx-auto px-4 py-8'>
      <h1 className='text-3xl font-bold mb-8'>Manchester City Dashboard</h1>

      {/* Quick Stats */}
      <Row
        gutter={[16, 16]}
        className='mb-8'>
        <Col
          xs={24}
          sm={12}
          lg={6}>
          <Card>
            <Statistic
              title='Next Match'
              value='vs Liverpool'
              prefix={<CalendarOutlined />}
              suffix='Jan 30, 2024'
            />
          </Card>
        </Col>
        <Col
          xs={24}
          sm={12}
          lg={6}>
          <Card>
            <Statistic
              title='Haaland Goals'
              value={25}
              prefix={<AimOutlined />}
              suffix='This Season'
            />
          </Card>
        </Col>
        <Col
          xs={24}
          sm={12}
          lg={6}>
          <Card>
            <Statistic
              title='League Position'
              value='2nd'
              prefix={<TrophyOutlined />}
              suffix='Premier League'
            />
          </Card>
        </Col>
        <Col
          xs={24}
          sm={12}
          lg={6}>
          <Card>
            <Statistic
              title='Form'
              value='WWDWW'
              prefix={<TrophyOutlined />}
              suffix='Last 5 Games'
            />
          </Card>
        </Col>
      </Row>

      {/* Recent News */}
      <h2 className='text-2xl font-semibold mb-4'>Recent News</h2>
      <Row
        gutter={[16, 16]}
        className='mb-8'>
        <Col
          xs={24}
          md={8}>
          <Card
            title="Haaland's Hat-trick Heroics"
            extra={
              <a
                href='#'
                className='text-blue-600'>
                Match Report
              </a>
            }>
            <p>
              Erling Haaland scores three as City demolish opponents in style.
            </p>
            <div className='text-sm text-gray-500 mt-4'>2024-01-25</div>
          </Card>
        </Col>
        <Col
          xs={24}
          md={8}>
          <Card
            title='Injury Update'
            extra={
              <a
                href='#'
                className='text-blue-600'>
                Team News
              </a>
            }>
            <p>Team news and injury updates ahead of the next fixture.</p>
            <div className='text-sm text-gray-500 mt-4'>2024-01-24</div>
          </Card>
        </Col>
        <Col
          xs={24}
          md={8}>
          <Card
            title='Training Ground Report'
            extra={
              <a
                href='#'
                className='text-blue-600'>
                Training
              </a>
            }>
            <p>
              Behind the scenes look at City's preparation for upcoming matches.
            </p>
            <div className='text-sm text-gray-500 mt-4'>2024-01-23</div>
          </Card>
        </Col>
      </Row>

      {/* Quick Links */}
      <h2 className='text-2xl font-semibold mb-4'>Quick Links</h2>
      <Row gutter={[16, 16]}>
        {['Fixtures', 'Statistics', 'Players', 'Results'].map((title) => (
          <Col
            xs={12}
            md={6}
            key={title}>
            <Card
              hoverable
              className='text-center'>
              <UserOutlined style={{ fontSize: '24px' }} />
              <div className='mt-2 font-medium'>{title}</div>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default HomePage;
