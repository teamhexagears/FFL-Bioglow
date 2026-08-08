from pybricks.tools import multitask, run_task, wait, hub_menu

async def async_reset(robot):
    print("resetting...")
    await robot.right_attachment_reset()
    await robot.async_right_attachment_turn(-90)

async def reset_and_drive(robot):
    print("moving")
    await multitask(
        async_reset(robot),
        robot.async_move(1000)
    )

def m4(robot):
    run_task(reset_and_drive(robot))

    robot.turn(50)
