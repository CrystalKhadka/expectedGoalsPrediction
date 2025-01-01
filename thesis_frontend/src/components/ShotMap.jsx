import React from 'react';

const ShotMap = ({ shots }) => {
    // Constants for pitch dimensions
    const PITCH_WIDTH = 800;
    const PITCH_HEIGHT = 600;
    const GOAL_WIDTH = 80;
    const GOAL_HEIGHT = 240;

    return (
        <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-6">Shot Map</h2>

            <div className="w-full overflow-hidden">
                <svg
                    viewBox={`0 0 ${PITCH_WIDTH} ${PITCH_HEIGHT}`}
                    className="w-full h-auto"
                >
                    {/* Pitch Background */}
                    <rect
                        width={PITCH_WIDTH}
                        height={PITCH_HEIGHT}
                        fill="#2F7B2F"
                        stroke="white"
                        strokeWidth="2"
                    />

                    {/* Penalty Area */}
                    <rect
                        x={PITCH_WIDTH - 180}
                        y={(PITCH_HEIGHT - GOAL_HEIGHT) / 2}
                        width="180"
                        height={GOAL_HEIGHT}
                        fill="none"
                        stroke="white"
                        strokeWidth="2"
                    />

                    {/* Goal Box */}
                    <rect
                        x={PITCH_WIDTH - 60}
                        y={(PITCH_HEIGHT - GOAL_WIDTH) / 2}
                        width="60"
                        height={GOAL_WIDTH}
                        fill="none"
                        stroke="white"
                        strokeWidth="2"
                    />

                    {/* Center Circle */}
                    <circle
                        cx={PITCH_WIDTH / 2}
                        cy={PITCH_HEIGHT / 2}
                        r="60"
                        fill="none"
                        stroke="white"
                        strokeWidth="2"
                    />

                    {/* Shot Markers */}
                    {shots.map((shot) => (
                        <g key={shot.id}>
                            <circle
                                cx={shot.x * (PITCH_WIDTH / 100)}
                                cy={shot.y * (PITCH_HEIGHT / 100)}
                                r={shot.xG * 15} // Size based on xG
                                fill={shot.goal ? '#ef4444' : '#3b82f6'}
                                fillOpacity="0.6"
                                stroke={shot.goal ? '#dc2626' : '#2563eb'}
                                strokeWidth="2"
                            />
                            <text
                                x={shot.x * (PITCH_WIDTH / 100)}
                                y={(shot.y * (PITCH_HEIGHT / 100)) - 10}
                                textAnchor="middle"
                                fill="white"
                                fontSize="12"
                            >
                                {shot.minute}'
                            </text>
                        </g>
                    ))}
                </svg>

                {/* Legend */}
                <div className="flex justify-center space-x-8 mt-4">
                    <div className="flex items-center">
                        <div className="w-4 h-4 rounded-full bg-red-500 mr-2" />
                        <span>Goals</span>
                    </div>
                    <div className="flex items-center">
                        <div className="w-4 h-4 rounded-full bg-blue-500 mr-2" />
                        <span>Shots</span>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ShotMap;