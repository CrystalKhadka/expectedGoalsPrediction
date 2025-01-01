import React from 'react';
import { Calendar, MapPin, Users } from 'lucide-react';

const FixtureCard = ({ fixture }) => {
    return (
        <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-all duration-200">
            <div className="flex justify-between items-center mb-4">
                <span className="text-blue-600 font-semibold">{fixture.competition}</span>
                <div className="flex items-center text-gray-600">
                    <Calendar className="w-4 h-4 mr-2" />
                    <span>{fixture.date}</span>
                </div>
            </div>

            <div className="flex items-center justify-between mb-6">
                <div className="text-center flex-1">
                    <img
                        src={fixture.homeTeamLogo || "/placeholder-team.png"}
                        alt={fixture.homeTeam}
                        className="w-12 h-12 mx-auto mb-2"
                    />
                    <span className="font-semibold">{fixture.homeTeam}</span>
                </div>

                <div className="flex flex-col items-center mx-4">
                    <span className="text-2xl font-bold">{fixture.score || "vs"}</span>
                    <span className="text-sm text-gray-500">{fixture.time}</span>
                </div>

                <div className="text-center flex-1">
                    <img
                        src={fixture.awayTeamLogo || "/placeholder-team.png"}
                        alt={fixture.awayTeam}
                        className="w-12 h-12 mx-auto mb-2"
                    />
                    <span className="font-semibold">{fixture.awayTeam}</span>
                </div>
            </div>

            <div className="border-t pt-4">
                <div className="flex justify-between text-sm text-gray-600">
                    <div className="flex items-center">
                        <MapPin className="w-4 h-4 mr-1" />
                        <span>{fixture.venue}</span>
                    </div>
                    <div className="flex items-center">
                        <Users className="w-4 h-4 mr-1" />
                        <span>{fixture.attendance?.toLocaleString()}</span>
                    </div>
                </div>
            </div>

            {fixture.haalandPlayed && (
                <div className="mt-4 bg-green-50 rounded p-3">
                    <p className="text-sm text-green-700">
                        Haaland: {fixture.haalandGoals} goals, {fixture.haalandAssists} assists
                    </p>
                </div>
            )}
        </div>
    );
};

export default FixtureCard;