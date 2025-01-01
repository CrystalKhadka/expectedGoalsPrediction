import React from 'react';
import { Trophy, Calendar, User, Activity } from 'lucide-react';

const NavBar = () => {
    return (
        <nav className="bg-blue-600 p-4">
            <div className="container mx-auto flex justify-between items-center">
                <div className="flex items-center space-x-2">
                    <Trophy className="h-8 w-8 text-white" />
                    <span className="text-white text-xl font-bold">Man City Stats</span>
                </div>

                <div className="hidden md:flex space-x-6">
                    <NavLink icon={<Calendar className="h-5 w-5" />} text="Fixtures" />
                    <NavLink icon={<User className="h-5 w-5" />} text="Haaland Stats" />
                    <NavLink icon={<Activity className="h-5 w-5" />} text="Performance" />
                </div>
            </div>
        </nav>
    );
};

const NavLink = ({ icon, text }) => (
    <a
        href="#"
        className="flex items-center space-x-2 text-white hover:text-blue-200 transition-colors duration-200"
    >
        {icon}
        <span>{text}</span>
    </a>
);

export default NavBar;