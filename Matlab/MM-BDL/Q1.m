% 定义Loong数组长度
N = 223;

% 设置k的值
k = 0.55/(2 * pi); 
data = zeros(2 * 301, N);

% 设置极坐标图更新的时间间隔，单位是秒
pauseTime =0.3;

% 创建一个图形窗口
figure;

% t从1到300循环
for t = 0:300
    % 初始化Loong数组
    %t=300;
    Loong = zeros(2, N);
    % 初始化Loong[1][]为32*pi
    Loong(2, :) = 32 * pi;
    
    % 计算Loong的第一个元素
    Loong(1,1) = findFirstTheta(t);
    
    % % 计算Loong的第二个元素
    % temp = findNextTheta(Loong(1,1), 2.86);
    % if temp == -1000
    %     Loong(1,2) = 32*pi;
    % else
    %     Loong(1,2) = temp;
    %     % 计算Loong的第三到第223个元素
    %     for n = 3:N
    %         % disp(Loong(1,n-1))
    %         temp = findNextTheta(Loong(1,n-1), 1.65);
    % 
    %         if temp == -1000
    %             Loong(1,n) = 32*pi; 
    %             break
    %         else
    %             Loong(1,n) = temp;
    %         end
    %     end    
    % end

    % 计算极坐标下的r和theta
    Loong(2, :) = k * Loong(1, :);
    % r = k * validLoong;
    % theta = validLoong;
    
    
    Loongxy= zeros(2, N);
    Loongxy(1, :) = k*Loong(1, :).*cos(Loong(1, :));
    Loongxy(2, :) = k*Loong(2, :).*sin(Loong(2, :));

    data((t)*2+1, :) = Loongxy(1, :);
    data((t)*2+2, :) = Loongxy(2, :);

    % 清除当前图形窗口
    clf;

    % 在极坐标下作图
    polarplot(Loong(1, :), Loong(2, :), 'o'); % 绘制所有点

    % 单独绘制第一个点为红色
    hold on; % 保持当前图形，以便添加新图形
    polarplot(Loong(1, 1), Loong(2, 1), 'ro', 'MarkerSize', 8); % 第一个点用红色圆圈表示，可以调整MarkerSize大小

    % 更新图形窗口标题
    title(sprintf('t = %d', t));
    
    % 暂停一段时间再继续循环
    pause(pauseTime);
    disp(t);
    hold off; % 关闭hold on，为下一次循环准备
end

% 将data矩阵写入Excel文件
filename = 'xy4.xlsx';
writematrix(data, filename);