% 参数定义
L_head = 2.86;  % 龙头板长（米），减去两端的把手部分
L_body = 1.65;  % 龙身和龙尾板长（米），减去两端的把手部分
pitch = 0.55;   % 螺距（米）
v_head = 1;     % 龙头前把手速度（m/s）
theta0 = 16 * 2 * pi; % 螺线第16圈的初始角度
t_total = 300; % 总时间300秒
dt = 1; % 每秒计算
num_sections = 223;

% 计算龙头的初始半径和角速度
initial_radius_head = pitch * theta0 / (2 * pi); % 龙头初始半径
angular_velocity = v_head / initial_radius_head; % 角速度

% 初始化矩阵
time_steps = t_total + 1;
positions = cell(1, 2);
positions{1} = zeros(time_steps, num_sections);
positions{2} = zeros(time_steps, num_sections);

% 计算每节板凳的每秒位置
for t = 0:t_total
    % 计算龙头位置
    theta = theta0 - angular_velocity * t;
    r_head = pitch * theta / (2 * pi);
    positions{1}(t+1, 1) = r_head * cos(theta);
    positions{2}(t+1, 1) = r_head * sin(theta);
    
    % 计算每节板凳的位置
    current_theta = theta;
    current_radius = r_head;
    for i = 2:num_sections
        arc_length = (i == 2) * L_head + (i > 2) * L_body;
        delta_theta = arc_length / current_radius;
        current_theta = current_theta + delta_theta;
        current_radius = pitch * current_theta / (2 * pi);
        
        positions{1}(t+1, i) = current_radius * cos(current_theta);
        positions{2}(t+1, i) = current_radius * sin(current_theta);
    end
end

% 绘制螺旋线作为背景
theta_values = linspace(0, theta0, 1000);
r_values = pitch * theta_values / (2 * pi);
x_spiral = r_values .* cos(theta_values);
y_spiral = r_values .* sin(theta_values);

% 绘制每个t时刻的舞龙队状态和螺旋线背景
figure;
hold on;
plot(x_spiral, y_spiral, 'r-', 'LineWidth', 1.5); % 绘制红色螺旋线背景
title(['舞龙队的状态']);
xlabel('X 位置 (m)');
ylabel('Y 位置 (m)');
axis equal;
grid on;
hold off;

% 设置相同的刻度范围
xlim([min(x_spiral), max(x_spiral)]);
ylim([min(y_spiral), max(y_spiral)]);

for t = 0:t_total
    plot(positions{1}(t+1,:), positions{2}(t+1,:), 'bo-', 'MarkerSize', 4); % 绘制舞龙队的轨迹
    title(['舞龙队在第', num2str(t), '秒的状态']);
    pause(0.5); % 暂停0.5秒
end
