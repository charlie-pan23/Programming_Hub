function theta = findFirstTheta(t)
    % 引入符号计算库
    syms x

    % 定义常数k
    k = 0.55 / (2 * pi);
    t_1 = (0.55 / (8 * pi)) * (sqrt(1024 * pi^2 + 1) - 1)
    % 构造方程
    equation = x^2 == (8 * pi / 0.55 * (t_1-t)+1) ^ 2 - 1

    % 求解方程
    solutions = solve(equation, x);

    % 初始化theta为NaN，表示如果没有找到正解，则返回NaN
    theta = NaN;

    % 将解转换为数值
    numericSolutions = double(solutions);

    % 遍历所有解，寻找第一个正数解
    for idx = 1:length(numericSolutions)
        if numericSolutions(idx) > 0
            theta = vpa(numericSolutions(idx), 6);
            break; % 找到第一个正数解后退出循环
        end
    end

    % 返回theta值，如果没有找到正数解，将返回NaN
    return
end
