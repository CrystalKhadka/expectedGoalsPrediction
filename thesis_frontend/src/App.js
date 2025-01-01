import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import {
  HomeOutlined,
  MenuOutlined,
  ScheduleOutlined,
  TrophyOutlined,
  FacebookOutlined,
  TwitterOutlined,
  InstagramOutlined,
} from '@ant-design/icons';
import { Button, Layout, Menu, Drawer } from 'antd';

// Import pages
import FixturesPage from './pages/FixturesPage';
import HaalandStatsPage from './pages/HaalandStatsPage';
import MatchDetailsPage from './pages/MatchDetailsPage';
import HomePage from './pages/Homepage';

const { Header, Footer, Content } = Layout;

const App = () => {
  const [drawerVisible, setDrawerVisible] = useState(false);

  const menuItems = [
    {
      key: 'home',
      label: <Link to="/">Home</Link>,
      icon: <HomeOutlined />,
    },
    {
      key: 'fixtures',
      label: <Link to="/fixtures">Fixtures</Link>,
      icon: <ScheduleOutlined />,
    },
    {
      key: 'haaland',
      label: <Link to="/haaland">Haaland Stats</Link>,
      icon: <TrophyOutlined />,
    },
  ];

  return (
    <BrowserRouter>
      <Layout style={{ minHeight: '100vh' }}>
        {/* Header */}
        <Header style={{ backgroundColor: '#001529', padding: '0 16px' }}>
          <div className="container mx-auto flex justify-between items-center h-full">
            {/* Logo and Title */}
            <Link to="/" className="text-white flex items-center">
              <HomeOutlined style={{ fontSize: '24px', marginRight: '8px' }} />
              <span style={{ fontSize: '18px', fontWeight: 'bold' }}>Man City Dashboard</span>
            </Link>

            {/* Desktop Menu */}
            <Menu
              theme="dark"
              mode="horizontal"
              className="hidden md:flex"
              items={menuItems}
              style={{ backgroundColor: 'transparent', borderBottom: 'none' }}
            />

            {/* Mobile Menu Button */}
            <Button
              type="text"
              icon={<MenuOutlined />}
              className="md:hidden text-white"
              onClick={() => setDrawerVisible(true)}
            />
          </div>

          {/* Drawer for Mobile Menu */}
          <Drawer
            title="Man City Dashboard"
            placement="right"
            closable
            onClose={() => setDrawerVisible(false)}
            visible={drawerVisible}
          >
            <Menu mode="vertical" items={menuItems} />
          </Drawer>
        </Header>

        {/* Content */}
        <Content style={{ backgroundColor: '#f0f2f5', padding: '24px' }}>
          <div className="container mx-auto">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/fixtures" element={<FixturesPage />} />
              <Route path="/haaland" element={<HaalandStatsPage />} />
              <Route path="/match/:id" element={<MatchDetailsPage />} />
            </Routes>
          </div>
        </Content>

        {/* Footer */}
        <Footer style={{ backgroundColor: '#001529', color: '#fff', padding: '24px' }}>
          <div className="container mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {/* About Section */}
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '12px' }}>
                  Manchester City
                </h3>
                <p style={{ color: '#ccc' }}>
                  Follow the latest updates and statistics of Manchester City and Erling Haaland.
                </p>
              </div>

              {/* Quick Links */}
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '12px' }}>
                  Quick Links
                </h3>
                <Menu
                  theme="dark"
                  mode="vertical"
                  style={{ backgroundColor: 'transparent', border: 'none' }}
                  items={menuItems}
                />
              </div>

              {/* Social Media Links */}
              <div>
                <h3 style={{ fontSize: '16px', fontWeight: 'bold', marginBottom: '12px' }}>
                  Connect
                </h3>
                <p style={{ color: '#ccc' }}>Follow us on:</p>
                <div className="flex space-x-4">
                  <Button
                    shape="circle"
                    icon={<FacebookOutlined />}
                    href="https://facebook.com"
                    target="_blank"
                  />
                  <Button
                    shape="circle"
                    icon={<TwitterOutlined />}
                    href="https://twitter.com"
                    target="_blank"
                  />
                  <Button
                    shape="circle"
                    icon={<InstagramOutlined />}
                    href="https://instagram.com"
                    target="_blank"
                  />
                </div>
              </div>
            </div>
          </div>
        </Footer>
      </Layout>
    </BrowserRouter>
  );
};

export default App;
