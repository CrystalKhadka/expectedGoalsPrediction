import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Target, Award, Clock } from 'lucide-react';

const HaalandStats = ({ stats }) => {
    const performanceData = [
        { name: 'Goals', actual: stats.goals, expected: stats.expectedGoals },
        { name: 'Assists', actual: stats.assists, expected: stats.expectedAssists },
        { name: 'Shots', actual: stats.shots, expected: stats.expectedShots }
    ];

    return (
        <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-6">Haaland's Performance</h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <StatCard
                    icon={<Target className="w-6 h-6 text-blue-500" />}
                    title="Goals"
                    value={stats.goals}
                    subtitle="This Season"
                />
                <StatCard
                    icon={<Award className="w-6 h-6 text-green-500" />}
                    title="Assists"
                    value={stats.assists}
                    subtitle="This Season"
                />
                <StatCard
                    icon={<Clock className="w-6 h-6 text-purple-500" />}
                    title="Minutes Played"
                    value={stats.minutesPlayed}
                    subtitle="Total Minutes"
                />
            </div>

            <div className="h-80 mt-6">
                <h3 className="text-lg font-semibold mb-4">Performance vs Expected</h3>
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={performanceData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Bar dataKey="actual" fill="#2563eb" name="Actual" />
                        <Bar dataKey="expected" fill="#93c5fd" name="Expected" />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};

const StatCard = ({ icon, title, value, subtitle }) => (
    <div className="bg-gray-50 rounded-lg p-4">
        <div className="flex items-center mb-2">
            {icon}
            <h3 className="text-gray-600 ml-2">{title}</h3>
        </div>
        <div className="mt-2">
            <span className="text-3xl font-bold">{value}</span>
            <p className="text-sm text-gray-500 mt-1">{subtitle}</p>
        </div>
    </div>
);

export default HaalandStats;